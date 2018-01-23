# Tested with Python 3.6
# Install Pillow: pip install pillow
""" This script extracts exif data from JPEG images """
from PIL import Image
from PIL.ExifTags import TAGS
import sys

def getExif(img):
    res = {}
    exif = img._getexif()

    if exif == None:
        print("No exif data found!!")
        sys.exit(0)

    for k, v in exif.items():
        dcd = TAGS.get(k, k)
        res[dcd] = v

    return res

def main():
    try:
        imgName = input("Enter the name of the JPEG image: ")
        img = Image.open(imgName)

        if img.format != "JPEG":
            print("This only works with JPG images!!")
            sys.exit(0)
    except KeyboardInterrupt:
        print("\nExiting!!")
        sys.exit(0)
    except:
        print("Something went wrong!! check your input!!")
        sys.exit(0)

    print("Gathering exif data...")
    for k, v in getExif(img).items():
        try:
            v = v.decode("utf-8")
        except AttributeError:
            pass
        print(str(k) + ": ", v)

main()
