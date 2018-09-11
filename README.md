# preparing_training_images
This stage creates images overlayed with checkerboards to 
support the checkerboard detection stage of the vehicle platooning project.
In order to process, you need to download background images from the internet.
Deep Learning training requires typically several thousands images which can
be obtained e.g from image-net.org, kaggle or cocodataset.org.
An instruction for downloading from image-net can be found in the shell file downloadImages.sh. However, this method is time consuming since there can be
invalid links which require deletion. Thousands of images is demanded since their
variation can support the higher learning capability of the models.


You also need to download the checkerboard images with different size,
shapes and orientations. They can also be achieved by resize the original images
and rotate them.


## Prerequisite
Your computer should have preinstalled OpenCv.


## Processing
Let move the background images and checkerboard images into a folder. The folder 
should look like

<root_folder>
| --background
| --checkerboards

	
After downloading the images, you can run the checkerboard_main.py script to 
process the image. The process will check and resize the images to suitable size, 
overlay the checkerboard on top of the background. The name of the folder should be 

```
python3 /path/to/script/checkerboard_main.py /path/to/images/folers/images
```

<root_folder>
	|---background
	|---checkerboards



## Result
After running the process, you will obtain two folder checkerboad





