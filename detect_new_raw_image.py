import os
import sys

def get_file_names(directory:str) -> set:
	"""Loop over files in the directory and return a set of file names. Ignores sub-directories. Returns name WITHOUT extension"""
	image_names=[]
	for entry in os.scandir(directory):
		if entry.is_file():
			image_name=entry.name
			image_names.append(image_name)
	return set(image_names)

def compare_file_names(raw_directory:str='images/raw', processed_directory:str='images/processed') -> list:
	"""Compares two sets of file names from two different directories (a and b) and returns a set of missing file names with extensions.
	If there are no missing file names, returns a set of int 0"""
	raw_names = get_file_names(raw_directory)
	processed_names = get_file_names(processed_directory)
	#compare two sets to see if equal.
	raw_images_not_processed = raw_names.difference(processed_names)
	print(list(raw_images_not_processed))
	#if len(raw_images_not_processed)!=0:
	return list(raw_images_not_processed)
	#else:
	#	directory_a_names_not_in_b = set()
	#	return directory_a_names_not_in_b
	# debugging

compare_file_names()
