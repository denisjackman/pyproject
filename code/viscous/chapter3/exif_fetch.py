''' Exif data extraction from images'''
import sys
import argparse
import urllib
import urllib.request
import urllib.error
import urllib.parse
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS


def findImages(url):
    ''' Find all images on a web page'''
    print('[o] Finding images on ' + url)
    urlContent = urllib.request.urlopen(url).read()  # pylint: disable=R1732
    soup = BeautifulSoup(urlContent, features='html.parser')
    imgTags = soup.findAll('img')
    return imgTags


def downloadImage(imgTag):
    ''' Download an image and save it to the current directory'''
    try:
        print('[-] Dowloading image...')
        imgSrc = imgTag['src']
        print(f"[+] Image: {imgSrc}")
        imgContent = urllib.request.urlopen(imgSrc).read()  # pylint: disable=R1732
        print(f'[+] Downloaded image: {basename(urlsplit(imgSrc))}')
        imgFileName = f'data//{basename(urlsplit(imgSrc)[2])}'
        imgFile = open(imgFileName, 'wb')  # pylint: disable=R1732
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:  # pylint: disable=W0702
        return ''


def test_for_exif(imgFileName):
    ''' Test if an image has exif data'''
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()  # pylint: disable=W0212
        if info:
            print('[*] Found Exif data in image ' + imgFileName)
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
                if decoded == 'GPSInfo':
                    print('[*] ' + str(decoded) + ': ' + str(value))
    except:  # pylint: disable=W0702
        pass


def main():
    ''' Main function'''
    parser = argparse.ArgumentParser(usage='exifetch.py -u <target url>')
    parser.add_argument('-u', dest='url', type=str, help='specify url address')
    args = parser.parse_args()
    url = args.url
    if url is None:
        print(parser.usage)
        sys.exit(0)
    else:
        imgTags = findImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            test_for_exif(imgFileName)


if __name__ == '__main__':
    print('[+] Exif data extraction from images start')
    main()
    print('[+] Exif data extraction from images end')
