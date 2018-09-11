wget -c --tries=1 -i Desktop/image_preparation/background_list.txt -P Desktop/image_preparation/background
=======
#---------- Several collections of images can be used for backgrounds----------
# One way to downloading the images with wget. You need to open the Download URLs in image-net.org, 
# copy the urls into a .text file and then simply wait for the download. This method takes quite a lot of time
# and can be interrupted due to network traffics (upto hours for few thousands of images. Additionally, 
# you may need to delete invalid images.
# *** syntax: wget -c --tries=Num -i /path/to/your/list -P /path/to/the/storage
# *** -c   -> continue from the last download
# *** --tries=Num -> the number of tries you want to access a link before ignore it
# *** -i  -> to download to a folder
wget -c --tries=1 -i Desktop/checkerboards/background_list.txt -P Desktop/checkerboards/background

# A useful tool for downloading images, bounding box from Imagenet as well as preparing lableling can be found here
# https://github.com/tzutalin/ImageNet_Utils

# COCO (Common Objects in Context) is another more efficient method where images are already gathered in a collection.
# It saves your time and effort to download and needless to delete corrupted images. You can download some GB of 
# images within maybe half an hours. Besides, the images were already named in sequential order and shuffled randomly.
# Use the links at http://cocodataset.org/#download
