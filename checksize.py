import cv2
import os, sys

def checkSize(org_dir):
	""" Check and remove the checkerboards of which alpha masks have different dimension """
	project_dir  = os.path.dirname(os.path.normpath(org_dir))
	translated_checkerboard = os.path.join(project_dir,"translatedCheckerboards/")
	translated_alpha = os.path.join(project_dir, "translatedAlphas/")
	#path, dirs, fores = os.walk(checkerboard_dir).next()
	
	for image in os.listdir(translated_checkerboard):
		checkerboard = cv2.imread(os.path.join(translated_checkerboard, image))
		alpha = cv2.imread(os.path.join(translated_alpha, image))
		if (checkerboard.shape[0] != alpha.shape[0] or checkerboard.shape[1] != alpha.shape[1]):
			os.remove(os.path.join(translated_checkerboard, image))
			os.remove(os.path.join(translated_alpha, image))
			#print(image)
