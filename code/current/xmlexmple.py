'''  this is a tool to read xml'''
import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    '''this is a class to handle xml'''
    def __init__(self):
        super().__init__()
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # Call when an element starts
    def startElement(self, name, attrs):
        '''this is a function to handle xml'''
        self.CurrentData = name
        if name == "movie":
            print("*****Movie*****")
            title = attrs["title"]
            print(f"Title: {title}")

    # Call when an elements ends
    def endElement(self, name):
        '''this is a function to handle xml'''
        print(f"tag: {name}")
        if self.CurrentData == "type":
            print(f"Type: {self.type}")
        elif self.CurrentData == "format":
            print(f"Format: {self.format}")
        elif self.CurrentData == "year":
            print(f"Year: {self.year}")
        elif self.CurrentData == "rating":
            print(f"Rating: {self.rating}")
        elif self.CurrentData == "stars":
            print(f"Stars: {self.stars}")
        elif self.CurrentData == "description":
            print(f"Description: {self.description}")
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        '''this is a function to handle xml'''
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("Z:/Resources/xml/movies.xml")
