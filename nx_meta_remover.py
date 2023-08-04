#!/usr/bin/python3

from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
import os, sys, argparse
import piexif

def main(my_image):
    """
    Processes the given image, removing its metadata and adding a new copyright field.

    Args:
        my_image: str
            Path to the image file.

    Returns: None
    Outputs: Saves a new image with updated metadata and prints the filename.
    """
    image_f = my_image
    if os.path.isfile(image_f):
        directory, filename = os.path.split(image_f)
        print(f"[+] Selected image : {filename}")
        image = Image.open(image_f)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        if isinstance(image, JpegImageFile):
            exif_dict = {"0th": {piexif.ImageIFD.Copyright: "(c) Made with NxMetaRemover tool"}}
            exif_bytes = piexif.dump(exif_dict)
            image_without_exif.save(filename, exif=exif_bytes)
        else:
            image_without_exif.save(filename)

        sys.exit(0)
    else:
        print("[-] Enter a valid image.")
        sys.exit(1)

def arg():
    """
    Parses the command-line argument and calls the `main` function.

    Args: None
    Returns: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='my_image', help="Image to remove exif")
    args = parser.parse_args()
    main(args.my_image)

if __name__ == '__main__':
    """
    Entry point of the script.
    Calls the arg function to parse command line arguments and process the image.
    """
    arg()
