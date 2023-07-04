'''
    webcrawler
'''
import urllib.request

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        url = None
        end_quote = 0
    else:
        start_quote = page.find('"',start_link)
        end_quote = page.find('"',start_quote+1)
        url = page[start_quote+1:end_quote]
    return url, end_quote

def print_all_links(work_page):
    while True:
        result,end_point = get_next_target(work_page)
        if result:
            print(result)
            work_page = work_page[end_point:]
        else:
            break

def get_all_links(work_page):
    links=[]
    while True:
        url,end_point = get_next_target(work_page)
        if url:
            links.append(url)
            work_page = work_page[end_point:]
        else:
            break
    return links

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be
    # introduced in unit 4.
    try:
        return urllib.request.urlopen(url).read()
    except:
        return ""
    return ""

def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

print(crawl_web("http://xkcd.com/353",5))
