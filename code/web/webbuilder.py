"""
scratch.py

This program is a template for python programs
All this stuff at the top of the script
is just optional metadata;

TODO: finish adding the list of tages
TODO: divide the tags into html5 supported items
TODO: add a list of tags that are done
TDOD: code each tag into a subroutine
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/08 17:16:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def metadefinition():
    '''
        build a meta data section
    '''
    meta = ''
    meta += "<meta charset='utf-8-sig'>"
    meta += '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    meta += '<meta http-equiv="X-UA-Compatible" content="ie=edge">'
    meta += '<meta name="description" content="Python Scripting example">'
    meta += '<meta name="keywords" content="HTML, CSS, JavaScript">'
    meta += '<meta name="author" content="Denis Jackman">'
    return meta


def breakline():
    '''
    build a break line
    '''
    webpage = ''
    webpage += '<br>'
    return webpage


def bold(text):
    '''
        build a bold text
    '''
    webpage = ''
    webpage += f'<b>{text}</b>'
    return webpage


def cssdefintion():
    '''
        build a css style sheet
    '''
    css = ''
    css += '<style>'
    css += 'body {'
    css += 'background-color: black;'
    css += 'font-family: verdana;'
    css += 'font-size: 12px;'
    css += 'color: white;'
    css += '}'
    css += 'h1 {'
    css += 'font-size: 24px;'
    css += 'color: lightgreen;'
    css += 'text-align: center;'
    css += '}'
    css += 'p {'
    css += 'font-size: 20px;'
    css += 'font-family: verdana;'
    css += 'color: 	#E600FF;'
    css += '}'
    css += 'a {'
    css += 'background-color: gray;'
    css += 'color: lightblue;'
    css += 'font-size: 20px;'
    css += 'border: 2px solid white;'
    css += 'border-style: solid;'
    css += 'border-color: white;'
    css += '}'
    css += '</style>'
    return css


def pagetitle(titletext):
    '''
        build a title
    '''
    title = ''
    title += '<title>'
    title += titletext
    title += '</title>'
    return title


def pageheader():
    '''
    build the header of the web page
    '''
    title = 'Python Web Page Builder'
    webpage = ''
    webpage += '<!DOCTYPE html>'
    webpage += '<html>'
    webpage += '<head>'
    webpage += pagetitle(title)
    webpage += metadefinition()
    webpage += cssdefintion()
    webpage += '</head>'
    return webpage


def header1(subject):
    '''
    build the header of the web page
    '''
    webpage = ''
    webpage += '<h1>'
    webpage += subject
    webpage += '</h1>'
    return webpage


def buildpara(text):
    '''
        build a paragraph
    '''
    para = ''
    para += '<p>'
    para += text
    para += '</p>'
    return para


def buildlink(link, text):
    '''
        build a link
    '''
    webpage = ''
    webpage += f'<a href="{link}">{text}</a>'
    return webpage


def buildimage(imagepath, imagetext):
    '''
        build an image
    '''
    webpage = ''
    webpage += f'<img src="{imagepath}" alt="{imagetext}">'
    return webpage


def divstart(divid):
    '''
        build a div start
    '''
    div = ''
    div += f'<div id= "{divid}">'
    return div


def divend():
    '''
        build a div end
    '''
    div = ''
    div += '</div>'
    return div


def pagebody():
    '''
    build the body of the web page
    '''
    webpage = ''
    webpage += '<body>'
    webpage += header1('Python Web Builder')
    webpage += buildpara(f'This is a {bold("paragraph")}.')
    webpage += divstart('mainContent')
    webpage += header1('Main content')
    webpage += breakline()
    webpage += buildpara('This is a main content paragraph.')
    webpage += breakline()
    webpage += buildlink("https://www.w3schools.com",
                         'This is a link')
    webpage += breakline()
    webpage += buildimage("https://www.w3schools.com/images/w3schools_green.jpg",
                          'This is an image')
    webpage += breakline()
    webpage += divend()
    webpage += divstart('sidebar')
    webpage += header1('Sidebar Header')
    webpage += breakline()
    webpage += buildpara('This is a paragraph in the sidebar.')
    webpage += breakline()
    webpage += buildlink("https://www.w3schools.com",
                         f'This is a {bold("link")} in the sidebar')
    webpage += breakline()
    webpage += buildimage("https://www.w3schools.com/images/w3schools_green.jpg",
                          'This is an image in the sidebar')
    webpage += breakline()
    webpage += divend()
    webpage += '</body>'
    return webpage


def pagefooter():
    '''
    build the footer of the web page
    '''
    webpage = ''
    webpage += '</html>'
    return webpage


def build_page():
    '''
    build the web page
    '''
    webpage = ''
    webpage += pageheader()
    webpage += pagebody()
    webpage += pagefooter()
    return webpage


def tag_list():
    '''
        build a list of tags
        From https://www.w3schools.com/tags/default.asp
         Tag Description
        implemented:
            <meta>           Defines metadata about an HTML document
            <title>          Defines a title for the document
            <br>             Defines a single line break
            <b>              Defines bold text
            <style>          Defines style information for a document
            <head>           Defines information about the document
            <div>            Defines a section in a document
            <img>            Defines an image
            <a>              Defines a hyperlink
            <p>              Defines a paragraph
            <!DOCTYPE>       Defines the document type

        not implemented:
            '<!--...-->'     Defines a comment
            <abbr>           Defines an abbreviation or an acronym
            <address>        Defines contact information for the
                             author/owner of a document
            <area>           Defines an area inside an image-map
            <article>        Defines an article
            <aside>          Defines content aside from the page content
            <audio>          Defines sound content
            <base>           Specifies the base URL/target for all relative
                             URLs in a document
            <bdi>            Isolates a part of text that might be formatted
                             in a different direction from other text
                             outside it
            <bdo>            Overrides the current text direction
            <blockquote>     Defines a section that is quoted from another
                             source
            <body>           Defines the document's body
            <button>         Defines a clickable button
            <canvas>         Used to draw graphics, on the fly,
                            via scripting (usually JavaScript)
            <caption>        Defines a table caption
            <cite>           Defines the title of a work
            <code>           Defines a piece of computer code
            <col>            Specifies column properties for each column
                             within a <colgroup> element
            <colgroup>       Specifies a group of one or more columns in
                             a table for formatting
            <data>           Links the given content with a machine-readable
                             translation
            <dd>             Defines a description/value of a term in a
                             description list
            <details>        Defines additional details that the user can
                             view or hide
            <dfn>            Represents the defining instance of a term
            <dialog>         Defines a dialog box or window
            <dl>             Defines a description list
            <dt>             Defines a term/name in a description list
            <em>             Defines emphasized text
            <embed>          Defines a container for an external
                             (non-HTML) application
            <fieldset>       Groups related elements in a form
            <figcaption>     Defines a caption for a <figure> element
            <figure>         Specifies self-contained content
            <footer>         Defines a footer for a document or section
            <form>           Defines an HTML form for user input
            <h1> to <h6>     Defines HTML headings
            <header>         Defines a header for a document or section
            <hr>             Defines a thematic change in the content
            <html>           Defines the root of an HTML document
            <i>              Defines a part of text in an alternate voice
                             or mood
            <iframe>         Defines an inline frame
            <input>          Defines an input control
            <ins>            Defines a text that has been inserted into a
                             document
            <kbd>            Defines keyboard input
            <label>          Defines a label for an <input> element
            <legend>         Defines a caption for a <fieldset> element
            <li>             Defines a list item
            <link>           Defines the relationship between a document and
                             an external resource (most used to link to style
                             sheets)
            <main>           Specifies the main content of a document
            <map>            Defines a client-side image-map
            <mark>           Defines marked/highlighted text
            <meter>          Defines a scalar measurement within a known range
                             (a gauge)
            <nav>            Defines navigation links
            <noscript>       Defines an alternate content for users that do not
                             support client-side scripts
            <object>         Defines an embedded object
            <ol>             Defines an ordered list
            <optgroup>       Defines a group of related options in a drop-down
                             list
            <option>         Defines an option in a drop-down list
            <output>         Defines the result of a calculation
            <param>          Defines a parameter for an object
            <picture>        Defines a container for multiple image resources
            <pre>            Defines preformatted text
            <progress>       Represents the progress of a task
            <q>              Defines a short quotation
            <rp>             Defines what to show in browsers that do not
                             support ruby annotations
            <rt>             Defines an explanation/pronunciation of
                             characters (for East Asian typography)
            <ruby>           Defines a ruby annotation (for East
                             Asian typography)
            <s>              Defines text that is no longer correct
            <samp>           Defines sample output from a computer program
            <script>         Defines a client-side script
            <section>        Defines a section in a document
            <select>         Defines a drop-down list
            <small>          Defines smaller text
            <source>         Defines multiple media resources for media
                             elements (<video> and <audio>)
            <span>           Defines a section in a document
            <strong>         Defines important text
            <sub>            Defines subscripted text
            <summary>        Defines a visible heading for a <details> element
            <sup>            Defines superscripted text
            <svg>            Defines a container for SVG graphics
            <table>          Defines a table
            <tbody>          Groups the body content in a table
            <td>             Defines a cell in a table
            <template>       Defines a template
            <textarea>       Defines a multiline input control (text area)
            <tfoot>          Groups the footer content in a table
            <th>             Defines a header cell in a table
            <thead>          Groups the header content in a table
            <time>           Defines a date/time
            <tr>             Defines a row in a table
            <track>          Defines text tracks for media elements
                             (<video> and <audio>)
            <u>              Defines text that should be stylistically
                             different from normal text
            <ul>             Defines an unordered list
            <var>            Defines a variable
            <video>          Defines a video or movie
            <wbr>            Defines a possible line-break

            The following are not supported in HTML5:
            <acronym>        Not supported in HTML5. Use <abbr> instead.
                             Defines an acronym
            <applet>         Not supported in HTML5. Use <embed> or
                             <object> instead. Defines an embedded applet
            <basefont>       Not supported in HTML5. Use CSS instead.
                             Specifies a default color, size, and font
                             for all text in a document
            <big>            Not supported in HTML5. Use CSS instead.
                             Defines big text
            <center>         Not supported in HTML5. Use CSS instead.
                             Defines centered text
            <dir>            Not supported in HTML5. Use <ul> instead.
                             Defines a directory list
            <font>           Not supported in HTML5. Use CSS instead.
                             Defines font, color, and size for text
            <frame>          Not supported in HTML5. Defines a window
                             (a frame) in a frameset
            <frameset>       Not supported in HTML5. Defines a set of frames
            <noframes>       Not supported in HTML5. Defines an alternate
                             content for users that do not support frames
            <strike>         Not supported in HTML5. Use <del> or <s> instead.
                             Defines strikethrough text
            <tt>             Not supported in HTML5. Use CSS instead. Defines
                             teletype text

    '''


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    path = r'Z:\Resources\development\index.html'
    with open(path, "w", encoding='utf-8-sig') as file:
        file.write(build_page())
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
