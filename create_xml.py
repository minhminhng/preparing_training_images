from xml.etree.ElementTree import Element, ElementTree, SubElement, Comment, tostring
import os, sys

def writeXML(annotation_dir, par_path, fileName, w=0, h=0, d=0, xmi=0, ymi=0, xma=0, yma=0, trun = 0):
	out = open(annotation_dir + fileName + ".xml", 'w')
	annotation = Element('annotation')
	doc = ElementTree(annotation)
	folder = SubElement(annotation, 'folder')
	folder.text = os.path.basename(par_path)
	filename = SubElement(annotation, 'filename')
	filename.text = fileName
	path = SubElement(annotation, 'path')
	path.text = par_path
	source = SubElement(annotation, 'source')
	database = SubElement(source, 'database')
	database.text = "Unknown"
	size = SubElement(annotation, 'size')
	width = SubElement(size, 'width')
	width.text = str(w)
	height = SubElement(size, 'height')
	height.text = str(h)
	depth = SubElement(size, 'depth')
	depth.text = str(d)
	segmented = SubElement(annotation, 'segmented')
	segmented.text = "0"
	object = SubElement(annotation, 'object')
	name = SubElement(object, 'name')
	name.text = "checkerboard"
	pose = SubElement(object, 'pose')
	pose.text = "Unspecified"
	truncated = SubElement(object, 'truncated')
	truncated.text = str(trun)
	#occluded = SubElement(object, 'occluded')
	bndbox = SubElement(object, 'bndbox')
	xmin = SubElement(bndbox, 'xmin')
	xmin.text = str(xmi)
	ymin = SubElement(bndbox, 'ymin')
	ymin.text = str(ymi)
	xmax = SubElement(bndbox, 'xmax')
	xmax.text = str(xma)
	ymax = SubElement(bndbox, 'ymax')
	ymax.text = str(yma)
	difficult = SubElement(object, 'difficult')
	difficult.text = "0"	
	doc.write(out)
	out.close
