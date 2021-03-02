# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import os
# construct the argument parse and parse the arguments

# define the answer key which maps the question number
# to the correct answer
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

# load the image, convert it to grayscale, blur it
# slightly, then find edges
cur_dir = os.getcwd()

# image = cv2.imread(cur_dir+'./image_2021_2_18.png')
image = cv2.imread(cur_dir+'./input_trac_nghiem2.jpg')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# remove noise by blur image
blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
# apply canny edge detection algorithm
img_canny = cv2.Canny(blurred, 100, 200)
# find contours
cnts = cv2.findContours(img_canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)




def get_x_ver1(s):
    s = cv2.boundingRect(s)
    return s[0] * s[1]
def get_x(s):
   return s[1][0]



ans_blocks = []
x_old, y_old, w_old, h_old = 0, 0, 0, 0

# ensure that at least one contour was found
if len(cnts) > 0:
    # sort the contours according to their size in descending order
    cnts = sorted(cnts, key=get_x_ver1)

    # loop over the sorted contours
    for i, c in enumerate(cnts):
        x_curr, y_curr, w_curr, h_curr = cv2.boundingRect(c)
        if w_curr * h_curr > 100000:
            # check overlap contours
            check_xy_min = x_curr * y_curr - x_old * y_old
            check_xy_max = (x_curr + w_curr) * (y_curr + h_curr) - (x_old + w_old) * (y_old + h_old)

            # if list answer box is empty
            if len(ans_blocks) == 0:
                ans_blocks.append(
                    (gray_img[y_curr:y_curr + h_curr, x_curr:x_curr + w_curr], [x_curr, y_curr, w_curr, h_curr]))
                # update coordinates (x, y) and (height, width) of added contours
                x_old = x_curr
                y_old = y_curr
                w_old = w_curr
                h_old = h_curr
            elif check_xy_min > 20000 and check_xy_max > 20000:
                ans_blocks.append(
                    (gray_img[y_curr:y_curr + h_curr, x_curr:x_curr + w_curr], [x_curr, y_curr, w_curr, h_curr]))
                # update coordinates (x, y) and (height, width) of added contours
                x_old = x_curr
                y_old = y_curr
                w_old = w_curr
                h_old = h_curr
    # sort ans_blocks according to x coordinate
    sorted_ans_blocks = sorted(ans_blocks, key=get_x)



cv2.drawContours(image, cnts, -1, (0, 255, 0), 3)

# cv2.imshow('Contours', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Filename
filename = 'savedImage.jpg'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, image)
# cv2.imshow('img',img_canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(type(img_canny))
# print(sorted_ans_blocks[0])
#
#
# print(len(sorted_ans_blocks[0]))
# print(sorted_ans_blocks[0])
# #
#
# image=np.array(sorted_ans_blocks[1][0])
# #
# # print(image)
# cv2.imshow('img',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

