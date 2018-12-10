#!/usr/bin/env python

from numpy import sign
# import Image, ImageOps
from PIL import Image, ImageOps
from itertools import chain
import math
import numpy as np
import random

# ---------------------- MAKE IMAGE WITH BOARDER--------------------------------
# Set Size of your image
size = width, height = 300,300
# Make a new image a given color
img = Image.new("RGB", size, "white")
# Take made image and give it a "colored" boarder of "x" pixels
img_with_border = ImageOps.expand(img,border=10,fill='black')
img_with_border.show()
img_with_border.save('imaged-with-border.png')
# short version
# ImageOps.expand(Image.open('original-image.png'),border=300,fill='black').save('imaged-with-border.png')
# ---------------- MAKE IMAGE WITH BOARDER FOR A LIST --------------------------
# for i in list-of-images:
#   img = Image.open(i)
#   img_with_border = ImageOps.expand(img,border=300,fill='black')
#   img_with_border.save('bordered-%s' % i)
# -----------------------TURN IMAGE TO NP ARRAY---------------------------------
# Converts Image to grayscale, values from 0-255, otherwise image has 3 values (RGB)
img = Image.open('imaged-with-border.png').convert('L')
# Turn the image into a numpy array
np_img = np.array(img) # this will output a bunch of dam zeros but individual will be gray scale value?
# this will invert the numpy array - show you the true grayscale value but why?
np_img = ~np_img
# this will threshold all values and convert them to 0 or 1
np_img[np_img > 127] = 1
# ------------------------CREATE RANDOM POINTS----------------------------------
# Produce a random x variable from 0 to width of iamge
# first = random.randint(1,len(np_img[:,1]))
# Produce a random y variable from 0 to height of image
# second = random.randint(1,len(np_img[1,:]))
# Variable storing the random (x,y)
first = len(np_img[:,1])/2
second = len(np_img[1,:])/2
start = [first,second]
# Produce a random angle
# angle = random.randint(0,360)
angle = 0
radian = math.radians(angle)
time_step = 999999999
# end = [first+time_step*math.cos(radian),second+time_step*math.sin(radian)]
end = [first+1000,second]
# print np_img.shape
# print start
# print start[0], start[1]
# print sign(-100)
# print sign(1000)
# print angle
# print end
# print end[0], end[1]
# -------------------------Bresenham Algorithm----------------------------------
def covered_cells(start, end):
    """
    Cells covered by a ray from the start cell to the end cell.  This implements Bresenham's algorithm.

    Arguments:
    start -- (x,y) position of the start cell
    end -- (x,y) position of the end cell
    """
    # We'll need the lengths of the ranges later on.
    x_range = end[0] - start[0]
    y_range = end[1] - start[1]

    # If the start and the end are the same point, then we don't do
    # anything.
    if x_range == 0 and y_range == 0:
        return
        yield

    # Step through x or y?  Pick the one with the longer absolute
    # range.
    if abs(x_range) > abs(y_range):
        y_step = float(y_range) / abs(float(x_range))
        y = float(start[1])
        # def my_range(start,end,step) - in our case its direction?
        for x in xrange(start[0], end[0], sign(x_range)):
            yield((x, int(round(y))))
            y += y_step
    else:
        x_step = float(x_range) / abs(float(y_range))
        x = float(start[0])
        for y in xrange(start[1], end[1], sign(y_range)):
            yield((int(round(x)), y))
            x += x_step
# ------------------------------------------------------------------------------

pixels = covered_cells(start,end)
# print(pixels)

for i in pixels:
    # print(i)
    if np_img[i] == 1:
        # print(i)
        end_point = i
        break

# print end_point
distance = math.sqrt( (end_point[0] - start[0])**2 + (end_point[1] - start[1])**2 )
print start
print end_point
print distance
print np_img.shape


# print distance
# if __name__ == '__main__':
#     print 'Should be a diagonal'
#     for p in covered_cells((0, 0), (10, 10)):
#         print ' ', p
#     print
#
#     print 'Should print no cells'
#     for p in covered_cells((0, 0), (0, 0)):
#         print p
#     print p
#
#     print 'some other angle'
#     for p in covered_cells((2, 3), (12, 6)):
#         print p
#     print
#
#     print 'some other angle'
#     for p in covered_cells((-5, 5), (-7, -22)):
#         print p
#     print
