'''
    xml script
'''
from xml.dom.minidom import parse


def main():
    '''
        main function
    '''
    doc = parse("Z:/Resources/xml/samplexml.xml")
    print(doc.nodeName)
    skills = doc.getElementsByTagName("skill")
    print(skills)


if __name__ == "__main__":
    main()
