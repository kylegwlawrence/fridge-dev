import os

def get_file_names(directory:str) -> set:
	"""Loop over files in the directory and return a set of file names. Ignores sub-directories"""
	files=[]
	for entry in os.scandir(directory):
		if entry.is_file():
			file_name=entry.name
			files.append(file_name)
	return set(files)

def compare_file_names(directory_a:str, directory_b:str) -> set:
	"""Compares two sets of file names from two different directories (a and b) and returns a set of missing file names with extensions.
	If there are no missing file names, returns an empty set"""
	directory_a_names = get_file_names(directory_a)
	directory_b_names = get_file_names(directory_b)
	#compare two sets to see if equal.
	directory_a_names_not_in_b = directory_a_names.difference(directory_b_names)
	return directory_a_names_not_in_b
