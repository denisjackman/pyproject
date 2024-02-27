
''' extract gif data '''
# gps_exif_getter.py
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif(item):
    """
    Returns a dictionary from the exif data of an PIL Image item.
    Also converts the GPS Tags
    """
    exif_data = {}
    image = Image.open(item)
    # pylint: disable=W0212
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data


if __name__ == "__main__":
    exif = get_exif("Z:/Resources/images/jester.jpg")
    print(exif)
