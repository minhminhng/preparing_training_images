#! /usr/bin/env python

import numpy as np
import imutils
import cv2
import os, sys
import random
from alpha_image import drawAlpha

def resizeImage(image, num, output_dir=""):
	"""Perform resizing on the images in the directory"""	
	size = random.randint(100, 200)
	r = float(size) / image.shape[1]
	dim = (size, int(image.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
	cv2.imwrite(output_dir+"checkerboard"+str(num)+".jpeg", resized)
	
def rotateImage(image, angle, name, num, output_dir=""):
	"""Perform rotation on the images in the directory"""
	rotated = imutils.rotate_bound(image, angle)
	# "This can result in different sizes of output images"
	cv2.imwrite(output_dir+"checkerboard"+str(num)+".jpeg", rotated)
	return rotated

def prepare_checkerboard(org_dir):
##-------------------------
	## Resize the checkerboard randomly
	# Create a directory to store resized checkerboards
	project_dir  = os.path.dirname(os.path.normpath(org_dir))  

	resized_dir = os.path.join(project_dir,"resizedCheckerboards/")
	try:
		os.stat(resized_dir)
	except:
		os.mkdir(resized_dir)
	# --- Another solution which will work but need 
	# to change the directory--- 
	#if not os.path.exists(os.path.join(dir_name, output_folder)):
		#print('yes')
		#os.mkdir(os.path.join(dir_name,output_folder))	# make the directory for storing the images 
	num = 0	
	# Resize the checkerboards
	for i in range(1,10):
		#num = 0
		for imageFile in os.listdir(org_dir):
			image = cv2.imread(os.path.join(org_dir,imageFile))
			resizeImage(image, num, resized_dir)
			num = num + 1
		
	##----------------------------
	## Draw alpha images of the checkerboards
	# Create a directory to store alpha images
	alpha_dir = os.path.join(project_dir,"alphaCheckerboards/")
	try:
		os.stat(alpha_dir)
	except:
		os.mkdir(alpha_dir)
	
	# Create alpha images of the checkerboards
	for imageFile in os.listdir(resized_dir):
		image = cv2.imread(os.path.join(resized_dir,imageFile))
		alphaName = os.path.splitext(imageFile)[0]
		drawAlpha(image, alphaName, alpha_dir)
		#resizeImage(image, alphaName, alpha_dir)
		
	##-----------------------------
	## Rotate checkerboards and relevant alpha images
	## in different angles
	# Create an output folder for rotated checkerboards	
	# and rotated alpha images
	translated_dir = os.path.join(project_dir,"translatedCheckerboards/")
	translated_dir2 = os.path.join(project_dir, "translatedAlphas/")
	try:
		os.stat(translated_dir)
	except:
		os.mkdir(translated_dir)
		 
	try:
		os.stat(translated_dir2)
	except:
		os.mkdir(translated_dir2)
	
	num = 0
	for imageFile in os.listdir(resized_dir):
		image = cv2.imread(os.path.join(resized_dir,imageFile))
		imageName = os.path.splitext(imageFile)[0]
		angle = random.randint(0, 90)
		rotateImage(image, angle, imageName, num, translated_dir)
		
		for alphaFile in os.listdir(alpha_dir):
			if alphaFile.startswith(imageName):
				alpha_Image = cv2.imread(os.path.join(alpha_dir,alphaFile))
				alphaName = os.path.splitext(alphaFile)[0]
				rotateImage(alpha_Image, angle, alphaName, num, translated_dir2)
		num = num+1
