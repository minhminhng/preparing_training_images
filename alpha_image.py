#! /usr/bin/env python
## Dealing with alpha images
import numpy as np
import imutils
import cv2
import os, sys
import random
#from checkerboard_prepare import rotateImage 

def drawAlpha(image, alphaName, output_dir=""):
	"""Perform resizing on the images in the directory"""	
	alphaImage = np.zeros(image.shape[:2], dtype = "uint8")
	cv2.rectangle(alphaImage, (0,0), (image.shape[1], image.shape[0]),255, -1)
	cv2.imwrite(output_dir+alphaName+
				"_al"+".jpeg", alphaImage)
	
#def rotateAlpha(image, angle, name, num, output_dir=""):
	#"""Perform rotation on the images in the directory"""
	#rotateImage(image, angle, name, num, output_dir)
	
