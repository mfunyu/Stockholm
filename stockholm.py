#!/usr/bin/python3
import argparse
import os

TARGET_DIR = "infection"
EXTENSIONS_FILE = "wannacry_file_extensions.txt"

class Flags():
	version = False
	reverse = False
	silent = False

def error_exit(msg):
	print(f'Error:', msg)
	exit(1)

def decrypt(files):
	print(files)
	return

def encrypt(files):
	print(files)
	return

def get_targets(dir_path, files, exts):
	contents = os.listdir(dir_path)
	for f in contents:
		filename = dir_path + "/" + f
		if not os.path.isfile(filename):
			get_targets(filename, files, exts)
		ext_idx = filename.rfind(".")
		if ext_idx >= 0 and filename[ext_idx:] in exts:
			files.append(filename)

def get_extensions():
	try:
		with open(EXTENSIONS_FILE, 'r') as f:
			contents = f.readlines()
		extensions = set()
		for line in contents:
			extensions.add(line.strip())
		return extensions
	except Exception as e:
		error_exit(e)

def check_directory():
	try:
		home = os.path.expanduser('~')
		dir_path = home + "/" + TARGET_DIR
		if not os.path.exists(dir_path):
			error_exit(f"directory '{TARGET_DIR}' does not exist")
		return dir_path
	except Exception as e:
		error_exit(e)

def Stockholm():
	dir_path = check_directory()
	exts = get_extensions()
	files = []
	get_targets(dir_path, files, exts)
	if not files:
		error_exit(f"target files does not exist")

	if Flags.reverse:
		encrypt(files)
	else:
		decrypt(files)


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--version", action="store_true",
						help="show the version of the program",)
	parser.add_argument("-r", "--reverse", metavar="KEY",
						help="reverse the infection using the key")
	parser.add_argument("-s", "--silent", action="store_true",
						help="the program will not produce any output")
	args = parser.parse_args()
	print(args)
	if args.version:
		Flags.version = True
	if args.reverse:
		Flags.reverse = True
	if args.silent:
		Flags.silent = True

def main():
	parse_args()
	if Flags.version:
		print('Stockholm 1.0.0')
	else:
		Stockholm()
	print(Flags.version, Flags.reverse, Flags.silent)

main()
