''' xml test'''
import xml.dom.minidom
import math

def main():
    ''' main'''
    hexxmldoc = xml.dom.minidom.parse('y:/pyproject/scratch/project/hexagonAll_sheet.xml')
    print(f'hexxmldoc: {hexxmldoc}')
    print(f'hexxmldoc.nodeName: {hexxmldoc.nodeName}')
    print(f'hexxmldoc.childNodes: {hexxmldoc.childNodes}')
    itemlist = hexxmldoc.getElementsByTagName('SubTexture')
    for item in itemlist:
        print(f'item: {item.attributes["name"].value} {item.attributes["x"].value} {item.attributes["y"].value} {item.attributes["width"].value} {item.attributes["height"].value}')
    height = 140
    print(f'Height : {height} ')
    print(f'width : {math.sqrt(3) * (height/2)}')
    print(f'vert : {3/4 * height}')

if __name__ == '__main__':
    main()