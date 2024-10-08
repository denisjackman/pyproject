#!/usr/bin/env python

""" This is a modified version of James Mills' original recipe. """

import re
import sys
import time
import math
import urllib.request
import urllib.parse
import argparse
import hashlib
from html import escape

import multiprocessing as mp

from bs4 import BeautifulSoup


class Link():
    '''
        link object to be used in the graph
    '''
    def __init__(self, src, dst, link_type):
        self.src = src
        self.dst = dst
        self.link_type = link_type

    def __hash__(self):
        return hash((self.src, self.dst, self.link_type))

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.link_type == other.link_type)

    def __str__(self):
        return self.src + " -> " + self.dst


class Crawler():
    '''
        crawler object to be used in the graph
    '''
    def __init__(self,
                 root,
                 depth_limit,
                 confine=None,
                 exclude=None,
                 locked=True,
                 filter_seen=True):
        self.root = root
        self.host = urllib.parse.urlparse(root)[1]

        # Data for filters:
        self.depth_limit = depth_limit
        # Max depth (number of hops from root)
        self.locked = locked
        # Limit search to a single host?
        self.confine_prefix = confine
        # Limit search to this prefix
        self.exclude_prefixes = exclude
        # URL prefixes NOT to visit

        self.urls_seen = set()
        # Used to avoid putting duplicates in queue
        self.urls_remembered = set()
        # For reporting to user
        self.visited_links = set()
        # Used to avoid re-processing a page
        self.links_remembered = set()
        # For reporting to user

        self.num_links = 0
        # Links found (and not excluded by filters)
        self.num_followed = 0
        # Links followed.

        # Pre-visit filters:  Only visit a URL if it passes these tests
        self.pre_visit_filters = [self._prefix_ok,
                                  self._exclude_ok,
                                  self._not_visited,
                                  self._same_host]

        # Out-url filters: When examining a visited page, only process
        # links where the target matches these filters.
        if filter_seen:
            self.out_url_filters = [self._prefix_ok,
                                    self._same_host]
        else:
            self.out_url_filters = []

    def _pre_visit_url_condense(self, url):

        """ Reduce (condense) URLs into some canonical form before
        visiting.  All occurrences of equivalent URLs are treated as
        identical.

        All this does is strip the fragment component from URLs,
        so that http://foo.com/blah.html#baz becomes
        http://foo.com/blah.html """

        base, frag = urllib.parse.urldefrag(url)
        return base

    # URL Filtering functions.  These all use information from the
    # state of the Crawler to evaluate whether a given URL should be
    # used in some context.  Return value of True indicates that the
    # URL should be used.

    def _prefix_ok(self, url):
        """Pass if the URL has the correct prefix, or none is specified"""
        return (self.confine_prefix is None or url.startswith(self.confine_prefix))

    def _exclude_ok(self, url):
        """Pass if the URL does not match any exclude patterns"""
        prefixes_ok = [not url.startswith(p) for p in self.exclude_prefixes]
        return all(prefixes_ok)

    def _not_visited(self, url):
        """Pass if the URL has not already been visited"""
        return url not in self.visited_links

    def _same_host(self, url):
        """Pass if the URL is on the same host as the root URL"""
        try:
            host = urllib.parse.urlparse(url)[1]
            return re.match(f" {self.host} {host}", re.IGNORECASE)
        except Exception as e:
            print(sys.stderr, f"ERROR: Can't process url '{url}' ({e})")
            return False

    def crawlerName(self):
        ''' a second public method '''
        return True

    def crawl(self):

        """ Main function in the crawling process.  Core algorithm is:

        q <- starting page
        while q not empty:
           url <- q.get()
           if url is new and suitable:
              page <- fetch(url)
              q.put(urls found in page)
           else:
              nothing

        new and suitable means that we don't re-visit URLs we've seen
        already fetched, and user-supplied criteria like maximum
        search depth are checked. """

        q = mp.Queue()
        q.put((self.root, 0))

        while not q.empty():  # pylint: disable=too-many-nested-blocks
            this_url, depth = q.get()

            # Non-URL-specific filter: Discard anything over depth limit
            if depth > self.depth_limit:
                continue

            # Apply URL-based filters.
            do_not_follow = [f for f in self.pre_visit_filters if not f(this_url)]

            # Special-case depth 0 (starting URL)
            if depth == 0 and [] != do_not_follow:
                print(sys.stderr, "Whoops! Starting URL %s rejected by the following filters:", do_not_follow)

            # If no filters failed
            # (that is, all passed), process URL

            if [] == do_not_follow:
                try:
                    self.visited_links.add(this_url)
                    self.num_followed += 1
                    page = Fetcher(this_url)
                    page.fetch()
                    for link_url in [self._pre_visit_url_condense(item) for item in page.out_links()]:
                        if link_url not in self.urls_seen:
                            q.put((link_url, depth+1))
                            self.urls_seen.add(link_url)

                        do_not_remember = [f for f in self.out_url_filters if not f(link_url)]
                        if [] == do_not_remember:
                            self.num_links += 1
                            self.urls_remembered.add(link_url)
                            link = Link(this_url, link_url, "href")
                            if link not in self.links_remembered:
                                self.links_remembered.add(link)
                except Exception as e:
                    print(sys.stderr, f"ERROR: Can't process url {this_url} ({e})")


class OpaqueDataException (Exception):
    '''
    Exception to be raised when the
    data is not in the expected format '''
    def __init__(self, message, mimetype, url):
        Exception.__init__(self, message)
        self.mimetype = mimetype
        self.url = url


class Fetcher():
    """
    The name Fetcher is a slight misnomer:
    This class retrieves and interprets web pages."""

    def __init__(self, url):
        self.url = url
        self.out_urls = []

    def __getitem__(self, x):
        return self.out_urls[x]

    def out_links(self):
        '''
        Return a list of all the URLs found on the page.
        '''
        return self.out_urls

    def _open(self):
        url = self.url
        try:
            request = urllib.request.urlopen(url)  # pylint: disable=consider-using-with
            handle = urllib.request.build_opener()
        except IOError:
            return None
        return (request, handle)

    def fetch(self):
        ''' fetch the url and parse the results '''
        request, handle = self._open()
        # self._addHeaders(request)
        if handle:
            try:
                data = handle.open(request)
                mime_type = data.info().gettype()
                url = data.geturl()
                if mime_type != "text/html":
                    raise OpaqueDataException(f"Not interested in files of type {mime_type} ({url})", mime_type, url)
                content = data.read()
                soup = BeautifulSoup(content)
                tags = soup('a')
            except urllib.request.HTTPError as error:
                if error.code == 404:
                    print(f"ERROR: {error} -> {error.url}",
                          sys.stderr)
                    return
                print(f"ERROR: {error}", sys.stderr)
                tags = []
            except urllib.request.URLError as error:
                print(f"ERROR: {error}", sys.stderr)
                tags = []
            except OpaqueDataException as error:
                print(f"Skipping {error.url}, has type {error.mimetype}",
                      sys.stderr)
                tags = []
            for tag in tags:
                href = tag.get("href")
                if href is not None:
                    url = urllib.parse.urljoin(self.url, escape(href))
                    if url not in self:
                        self.out_urls.append(url)


def getLinks(glurl):
    '''
    Returns a list of links from a given url
    '''
    page = Fetcher(glurl)
    page.fetch()

    j = 1
    for i, listurl in enumerate(page):
        if listurl.find("http") >= 0:
            print(f"{j} {listurl}")
            j += 1


def parse_options():
    """parse_options() -> opts, args

    Parse any command-line options given returning both
    the parsed options and arguments.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-q",
                        "--quiet",
                        action="store_true",
                        default=False,
                        dest="quiet",
                        help="Enable quiet mode")

    parser.add_argument("-l",
                        "--links",
                        action="store_true",
                        default=False,
                        dest="links",
                        help="Get links for specified url only")

    parser.add_argument("-d",
                        "--depth",
                        action="store",
                        type="int",
                        default=30,
                        dest="depth_limit",
                        help="Maximum depth to traverse")

    parser.add_argument("-c",
                        "--confine",
                        action="store",
                        type="string",
                        dest="confine",
                        help="Confine crawl to specified prefix")

    parser.add_argument("-x",
                        "--exclude",
                        action="append",
                        type="string",
                        dest="exclude",
                        default=[],
                        help="Exclude URLs by prefix")

    parser.add_argument("-L",
                        "--show-links",
                        action="store_true",
                        default=False,
                        dest="out_links",
                        help="Output links found")

    parser.add_argument("-u",
                        "--show-urls",
                        action="store_true",
                        default=False,
                        dest="out_urls",
                        help="Output URLs found")

    parser.add_argument("-D",
                        "--dot",
                        action="store_true",
                        default=False,
                        dest="out_dot",
                        help="Output Graphviz dot file")

    opts, args = parser.parse_args()

    if len(args) < 1:
        parser.print_help(sys.stderr)
        raise SystemExit(1)

    if opts.out_links and opts.out_urls:
        parser.print_help(sys.stderr)
        parser.error("options -L and -u are mutually exclusive")

    return opts, args


class DotWriter:

    """ Formats a collection of Link objects as a Graphviz (Dot)
    graph.  Mostly, this means creating a node for each URL with a
    name which Graphviz will accept, and declaring links between those
    nodes."""

    def __init__(self):
        self.node_alias = {}

    def _safe_alias(self, url, silent=False):

        """Translate URLs into unique strings guaranteed to be safe as
        node names in the Graphviz language.  Currently, that's based
        on the md5 digest, in hexadecimal."""

        if url in self.node_alias:
            return self.node_alias[url]
        m = hashlib.md5()
        m.update(url)
        name = "N"+m.hexdigest()
        self.node_alias[url] = name
        if not silent:
            print("\t{name} [label=\"{url}\"];")
        return name

    def asDot(self, links):

        """ Render a collection of Link objects as a Dot graph"""

        print("digraph Crawl {")
        print("\t edge [K=0.2, len=0.1];")
        for item in links:
            print("\t" + self._safe_alias(item.src) + " -> " + self._safe_alias(item.dst) + ";")
        print("}")

    def DWName(self):
        ''' public method '''
        return True


def main():
    ''' main function '''
    opts, args = parse_options()

    url = args[0]

    if opts.links:
        getLinks(url)
        raise SystemExit(0)

    depth_limit = opts.depth_limit
    confine_prefix = opts.confine
    exclude = opts.exclude

    sTime = time.time()

    print(f"Crawling {url} (Max Depth: {depth_limit})", file=sys.stderr)
    crawler = Crawler(url, depth_limit, confine_prefix, exclude)
    crawler.crawl()

    if opts.out_urls:
        print(f"\n {crawler.urls_seen} URLs found")

    if opts.out_links:
        print("\n".join([str(item) for item in crawler.links_remembered]))

    if opts.out_dot:
        d = DotWriter()
        d.asDot(crawler.links_remembered)

    eTime = time.time()
    tTime = eTime - sTime

    print(sys.stderr, f"Found:    {crawler.num_links}")
    print(sys.stderr, f"Followed: {crawler.num_followed}")
    print(sys.stderr, f"Stats:    {tTime} after {(int(math.ceil(float(crawler.num_links) / tTime)), tTime)}")


if __name__ == "__main__":
    main()
