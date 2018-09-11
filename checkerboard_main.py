import os, os.path
import sys
import six
import cv2
from checkerboard_prepare import prepare_checkerboard
from alpha_image import drawAlpha
import random
from blending import blending_checkerboard
from checksize import checkSize

if __name__ == "__main__":
		
	##-------------------------
	## Check if a directory is given
	try:	
		org_dir = sys.argv[1]	# passing the first argument as directory name
	except:
		print('Usage: python checkerboard_main.py <checkerboard_image_directory>')
	
	prepare_checkerboard(org_dir)
	checkSize(org_dir)
	blending_checkerboard(org_dir)
		
	
