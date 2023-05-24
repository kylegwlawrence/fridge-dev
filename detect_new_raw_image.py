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

def compare_file_names(raw_directory:str='images/raw', processed_directory:str='images/processed') -> list:
	"""Get a set of raw imagenames and a set of processed image names, compare the sets, and return 
	a list of raw image names that have not been processed. If all raw images have a match in the 
	processed images folder, return an empty set."""
	raw_names = get_file_names(raw_directory)
	processed_names = get_file_names(processed_directory)
	# compare equality between the two sets
	raw_images_not_processed = raw_names.difference(processed_names)
	print(list(raw_images_not_processed))
	return list(raw_images_not_processed)