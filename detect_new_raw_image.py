import os
import sys

def get_file_names(directory:str) -> set:
	"""Loop over files in the directory and return a set of file names. Ignores sub-directories.
	Returns a set of image names with extension"""
	image_names=[]
	for entry in os.scandir(directory):
		if entry.is_file():
			image_name=entry.name
			image_names.append(image_name)
	return set(image_names)