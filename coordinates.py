#!/usr/bin/env python

import numpy as np
from PIL import Image
import random

# img = value for the image itself
img = Image.open('colored.jpg')
img.show()
# convert image to an array of RGB values 
np_img = np.array(img)
x = len(np_img[:, 1])  # 626
y = len(np_img[1, :])  # 626
print x,y
# global cordinates
print np_img[0,0] # lower left corner # - [254 118 0] - orange - upper left corner
print np_img[x-1,0] # lower right corner - [255 167 192] - pink - upper right corner
print np_img[x-1,y-1]  # upper right corner - [164 222 210] - teal - lower right corner
print np_img[0,y-1] # upper left corner - [255 167 192] - pink - lower left corner
