import os

# read over files in a directory and return a set of file names without filetype
def get_file_names(directory:str) -> set:
	files=[]
	for entry in os.scandir(directory):
		if entry.is_file():
			file_name_type_removed=entry.name.split('.')[0]
			files.append(file_name_type_removed)
	return set(files)

def compare_file_names(directory_a:str, directory_b:str) -> set:
	directory_a_names = get_file_names(directory_a)
	directory_b_names = get_file_names(directory_b)
	#compare two sets to see if equal.
	if directory_a_names==directory_b_names:
		print("All raw images have been processed")
	#determine which in raw are not in processed and run those through transform function
	else:
		directory_a_names_not_in_b = directory_a_names.difference(directory_b_names)
		print(directory_a_names_not_in_b)
		return directory_a_names_not_in_b
