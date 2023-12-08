#!/usr/bin/python3
import argparse

class Flags():
	version = False
	reverse = False
	silent = False

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--version", action="store_true",
						help="show the version of the program",)
	parser.add_argument("-r", "--reverse", metavar="KEY",
						help="reverse the infection using the key")
	parser.add_argument("-s", "--silent", action="store_true",
						help="the program will not produce any output")
	args = parser.parse_args()

	if args.v:
		flags.version = True
	if args.r:
		flags.reverse = True
	if args.s:
		flags.silent = True

	return

def main():
	flags = parse_args()
	print(flags)

main()
