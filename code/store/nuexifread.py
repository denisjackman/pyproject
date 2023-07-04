
'''
    nuexifread
'''
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

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
    #print(GPSTAGS.get(266))
    #for key in exif_table['GPSInfo'].keys():
        #decode = GPSTAGS.get(266)
        #print(decode)
        #gps_info[decode] = exif_table['GPSInfo'][key]

    return gps_info

filename = 'Y:/Resources/images/jester.jpg'
exif = get_exif(filename)
# print(isinstance(img, Image.Image))
# print(img.size)
# print(img.format)
# print(img.mode)
# print(img.info.keys())
print(exif)
