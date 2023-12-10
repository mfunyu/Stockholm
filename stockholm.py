#!/usr/bin/python3
import argparse
import os

TARGET_DIR = "infection"

class Flags():
	version = False
	reverse = False
	silent = False

def error_exit(msg):
	print(f'Error:', msg)
	exit(1)

def decrypt():
	return

def encrypt():
	return

def check_directory():
	try:
		home = os.path.expanduser('~')
		directory = home + "/" + TARGET_DIR
		if not os.path.exists(directory):
			error_exit(f"directory '{TARGET_DIR}' does not exist")
	except Exception as e:
		error_exit(e)

def Stockholm():
	check_directory()
	
	if Flags.reverse:
		encrypt()
	else:
		decrypt()


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
