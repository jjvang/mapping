#!/usr/bin/env python

from PIL import Image


def main():
    filename = "/home/palantir/Desktop/image.png"
    image = Image.open(filename)
    size = width, height = image.size

    cordinate = x, y = 1, 1
    print(image.getpixel(cordinate))
    # Output: (0,0,0,255) @ x,y = 1,1
    # [Finished in 0.051s]
    # Band(R, G, B, alpha)
    # Output: (235, 30, 36, 255) @ 250,250
    # [Finished in 0.051s]
    # Output: (0, 0, 0, 255) @ 499,499
    # Output @ 500,500 does not work twice, works once
    # Pixel axis objects

    # 25,000 pixels -> 0.051s = 212seconds -> 3hrs 30minutes

    del image


if __name__ == '__main__':
    main()

# A tuple is a sequence of immutable Python objects. Tuples are sequences, just
# like lists. The differences between tuples and lists are, the tuples cannot be
# changed unlike lists and tuples use parentheses, whereas lists use square brackets.
#
# tup1 = ('physics', 'chemistry', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5 );
# tup3 = "a", "b", "c", "d";

# Image.getpixel(xy)
# Returns the pixel value at a given position.
#
# Parameters:	xy - The coordinate, given as (x, y).
# Returns:The pixel value. If the image is a multi-layer image,
#     this method returns a tuple.
