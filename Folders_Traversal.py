# run the file using python Folder_Traversal.py <folder_name>

import os, sys
import argparse

args = sys.argv
args.pop(0)
arg_parser = argparse.ArgumentParser("Help")
arg_parser.add_argument("file_type", type =str , help = "folder", default = 1)
file_type = sys.argv[0]

def process(file_type):
	filelist = []
	for root, dirs, files in os.walk(file_type):
		for file in files:
			filelist.append(os.path.join(root, file))


	for name in filelist:
		with open('F:\\file_name.txt', 'a') as f: // destination path
			f.write(name)
			f.write('\n')
			f.close()

	return 

process(file_type)

