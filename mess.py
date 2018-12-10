#!/usr/bin/env pyhton

import Image


def main():  # {
    Filename = "py.png"
    image = Image.open(Filename)
    size = width, height = image.size

    coordinate = x, y = 180, 69
    print image.getpixel(coordinate)

    del image
# }


if (_name_ == "_main_"):  # {
    main()
# }
