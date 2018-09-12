
import os, sys
import random
import cv2
from create_xml import writeXML
import numpy as np

def choose_topleft(background, foreground, alpha):
	""" The position of the checkerboard should be within the background
		and at least half of the checker board should be shown in the background """
	xsize = foreground.shape[0]
	ysize = foreground.shape[1]
	sas = 1		# Flag to check if the positions are satisfied
	while xsize > -1 and ysize > -1:
		# Get the parameters
		xmin = random.randint(0, background.shape[0])
		ymin = random.randint(0, background.shape[1])
		xmax = xmin + foreground.shape[0]
		
		# Limit the size of the bounding box within the size of background
		if xmax > background.shape[0]:
			xmax = background.shape[0]
		ymax = ymin + foreground.shape[1]
		if ymax > background.shape[1]:
			ymax = background.shape[1]
		
		# Limit the size of the checkerboard within the background
		xsize = background.shape[0] - xmin
		#print("sizex", xsize)
		if (xsize <= foreground.shape[0] / 2):
			sas = 0
			continue
		#sas = 1
		#foreground2 = foreground[0:xsize,:]
		#alpha2 = alpha[0:xsize,:]
		
		ysize = background.shape[1] - ymin
		#print("sizey", ysize)
		if (ysize <= foreground.shape[1] / 2):
			sas = 0
			continue
		
		foreground2 = foreground[0:xmax - xmin,0:ymax - ymin]
		alpha2 = alpha[0:xmax - xmin,0:ymax - ymin]
		sas = 1
		#foreground2 = foreground
		#alpha2 = alpha	
		if sas == 1:
			break
	
	#print(xmax - xmin)
	#print(ymax - ymin)		
	return xmin, xmax, ymin, ymax, foreground2, alpha2

def blending_checkerboard(org_dir):
	project_dir = os.path.dirname(os.path.normpath(org_dir))  
	background_dir = os.path.join(project_dir, "background")
	checkerboard_dir = os.path.join(project_dir, "translatedCheckerboards/")
	alpha_dir = os.path.join(project_dir, "translatedAlphas/")
	image_dir = os.path.join(project_dir,"images/")
	try:
		os.stat(image_dir)
	except:
		os.mkdir(image_dir)
	
	pos_image_dir = os.path.join(image_dir,"checkerboard/")
	neg_image_dir = os.path.join(image_dir,"no_checkerboard/")
	try:
		os.stat(pos_image_dir)
	except:
		os.mkdir(pos_image_dir)
	try:
		os.stat(neg_image_dir)
	except:
		os.mkdir(neg_image_dir)

			
	path, dirs, backs = os.walk(background_dir).next()
	num_background = len(backs)
	#num_background = int(num_background / 2)
	
	path, dirs, fores = os.walk(checkerboard_dir).next()
	num_foreground = len(fores)
		
	annotation_dir = project_dir + "/annotationss/"
	try:
		os.stat(annotation_dir)
	except:
		os.mkdir(annotation_dir)
	list_used = []
	i = 0
	while (i  < num_background):# - 400):
		## Use half of the backgrounds as positive images and 
		## the other half as negative images
		
		r1 = random.randint(0, num_foreground-1)
		r2 = random.randint(0, num_background-1)
		# Read the images
		foreground = cv2.imread(os.path.join(checkerboard_dir, fores[r1]))
		background = cv2.imread(os.path.join(background_dir, backs[r2]))
		while (foreground.shape[0] > background.shape[0] or foreground.shape[1] > background.shape[1]):
			r2 = random.randint(0, num_background-1)
			background = cv2.imread(os.path.join(background_dir, backs[r2]))
		list_used.append(backs[r2])
		#print(backs[r2])
		backName = os.path.splitext(backs[r2])[0]
		alpha = cv2.imread(os.path.join(alpha_dir, fores[r1]))
		
		# Convert the images to float
		foreground = foreground.astype(float)
		background = background.astype(float)
		
		# Normalize the alpha mask to set the intensity between 0 and 1
		alpha = alpha.astype(float)/255
		
		xmin, xmax, ymin, ymax, foreground2, alpha = choose_topleft(background, foreground, alpha)
		
		#print(foreground.shape)
		#print(alpha.shape)
		
		foreground2 = cv2.multiply(alpha, foreground2)
		background2 = cv2.multiply(1 - alpha, background[xmin:xmax,ymin:ymax])
		outImage = cv2.add(foreground2, background2)
		background[xmin:xmax, ymin:ymax] = outImage
		
		#cv2.imshow("Foreground b4", foreground/255)
		#cv2.imshow("Background", background/255)
		##cv2.imshow("Alpha", alpha)
		#cv2.imshow("Foreground", foreground/255)
		#cv2.waitKey(0)
		cv2.imwrite(pos_image_dir+backName+".jpeg", background)
		# Create xml file
		trun = 0
		if (xmax-xmin+1 < foreground.shape[0] or ymax-ymin+1 < foreground.shape[1]):
			trun = 1
		writeXML(annotation_dir, background_dir, backs[r2], 
				background.shape[1], background.shape[0], background.shape[2],
				ymin, xmin, ymax, xmax, trun)
		i = i + 1
	
	for imageFile in os.listdir(background_dir):
		if imageFile in list_used:
			continue
		else:
			image = cv2.imread(os.path.join(background_dir, imageFile))
			cv2.imwrite(neg_image_dir+imageFile+".jpeg", image)
		
