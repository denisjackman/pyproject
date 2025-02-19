
'''
    nuexifread
'''
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(image_file_path):
    '''
        get exif data
    '''
    exif_table = {}
    image = Image.open(image_file_path)
    info = image.getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value

    gps_info = {}
    print(exif_table['GPSInfo'])

    return gps_info


def main():
    ''' main function '''
    filename = 'Z:/Resources/images/jester.jpg'
    exif = get_exif(filename)
    print(exif)


if __name__ == "__main__":
    main()
