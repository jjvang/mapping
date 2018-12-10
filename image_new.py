#!/usr/bin/env python
# Every python controller needs these lines
# Line above makes sure your script is excuted as a python script

from PIL import Image
# This statement allows you to use the Image Library

# THIS SECTION ONLY SET UP VARIABLES AND DEFINE FUNCTIONS


def main():
    size = width, height = 300, 300  # this is in pixels
    # image = Image.new("RGB", size, "red")
    filename = "checkmark.jpg"
    image = Image.open(filename)
    image.convert("1").show()
    # size2 = width, height = 296, 296  # this is in pixels
    # image2 = Image.new("RGB", size, "blue")
    # PIL.Image.new(mode, size, color=0)
    # image supports all the html color palet / note it is not case sensitive
    # image = Image.new("RGB",size, "hsl(0%, 100%, 0%)")
    # hsl = hue saturation lightness

    # DO NOT USE (-) from copy/paste it could crash your code
    # Watch out for weird characters which you could of copied and pasted
    # Potentially not aligned with the ASCII TABLE

    # mode - The mode to use for the new image. See: Modes.
    # size - A 2-tuple, containing (width, height) in pixels.
    # color - What color to use for the image. Default is black. If given, this
    # should be a single integer or floating point value for single-band modes
    # and a tuple for multi-band modes (one value per band). When creating RGB
    # images, you can also use color strings as supported by the ImageColor
    # module. If the color is None, the image is not initialised.

    # image.show()
    # image2.show()
    # Image.show(title=None, command=None)
    # This will display a black screen from image magic

    del image
    del image2
    # This will delete the image so it is not saved


# THIS SECTION WILL EXCUTE FUNCTIONS IF THE MODULE IS INDEED MAIN
if (__name__ == "__main__"):
    main()

# Types of modes
# The mode of an image defines the type and depth of a pixel in the image.
# The current release supports the following standard modes:

# 1 (1-bit pixels, black and white, stored with one pixel per byte)
# L (8-bit pixels, black and white)
# P (8-bit pixels, mapped to any other mode using a color palette)
# RGB (3x8-bit pixels, true color)
# RGBA (4x8-bit pixels, true color with transparency mask)
# CMYK (4x8-bit pixels, color separation)
# YCbCr (3x8-bit pixels, color video format)
# Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
# LAB (3x8-bit pixels, the L*a*b color space)
# HSV (3x8-bit pixels, Hue, Saturation, Value color space)
# I (32-bit signed integer pixels)
# F (32-bit floating point pixels)
