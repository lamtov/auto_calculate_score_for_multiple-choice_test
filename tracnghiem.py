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

image = cv2.imread(cur_dir+'./omr_test_01.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)
cv2.imshow('img',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # find contours in the edge map, then initialize
# # the contour that corresponds to the document
# cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# docCnt = None
# # ensure that at least one contour was found
# if len(cnts) > 0:
# 	# sort the contours according to their size in
# 	# descending order
# 	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
# 	# loop over the sorted contours
# 	for c in cnts:
# 		# approximate the contour
# 		peri = cv2.arcLength(c, True)
# 		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
# 		# if our approximated contour has four points,
# 		# then we can assume we have found the paper
# 		if len(approx) == 4:
# 			docCnt = approx
# 			break
#



def get_sbd(image_sbd, output_image):

	image = image_sbd
	height, width, channels = image.shape
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255,
						   cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


	filename = output_image
	sbd=[]
	for i in range(0,10):
		min=100000
		max =0
		pos=-1
		for j in range(0,10):

			cropx=i*int(width/10)
			cropy=j*int(height/10)
			square_image=thresh[cropx:cropx+int(width/10), cropy:cropy+int(height/10)]
			# print(square_image)
			cv2.imshow("cropped", square_image)
			cv2.waitKey(0)
			total =cv2.countNonZero(square_image)
			if total> max:
				max=total
				pos=j
			if total < min:
				min= total
		if min/max > 0.7:
			pos = -1
		sbd.append(pos)
	return sbd


