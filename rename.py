import os, os.path
import sys	# use for passing arguments
#import cv2

""" 
Renames the filenames within the same directory to be Unix friendly
(1) new file name start with 'background'
(2) files are enumerated
Usage:
python rename.py
"""

## Specify valid extensions
valid_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]

## Check if a directory is given
try:	
	dir_name = sys.argv[1]	# passing the first argument as directory name
except:
	print('Please pass directory name')
	
## check if the start of the new name is provided
try:	
	startname = sys.argv[2]	# passing the first argument as directory name
except:
	print('Please give new starting of name')

path =  dir_name #os.getcwd()
filenames = os.listdir(path)
start = "background"

i = 1242

for filename in filenames:
	ext = os.path.splitext(filename)[1]
	if ext.lower() not in valid_extensions:
		os.remove(os.path.join(path,filename))
		continue
	if not filename.startswith('background'):
	# syntax: os.rename(directory_and_name_of_file, directory_and_name_of_new_file)
		os.rename(os.path.join(path, filename), os.path.join(path, startname + str(i).zfill(4) + ext))
	# zfill: padding the term with 0 to the left
	i = i + 1
	
#i = 0

#for i,imagePath in image_path_list:	
	#if not filename.startswith(startname):
		#image = cv2.imread(imagePath)
		#if image is not None:		
			#os.rename(os.path.join(path,filename), os.path.join(path, startname + str(i).zfill(3) +ext))
		#i = i + 1
