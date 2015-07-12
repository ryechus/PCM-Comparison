from __future__ import division
import sys
from os.path import exists, realpath
import argparse
import audiotools
import math
import re

import e3


def get_frames(filename):
	audio = audiotools.open(filename.name)
	audiofile = audiotools.Filename(filename.name)
	reader = audiotools.PCMReader(audiofile.open('r'), audio.sample_rate(), 2, audio.channels(), audio.bits_per_sample())
	sr = audio.sample_rate()
	frames = audio.total_frames()

	highest_prime = e3.main(frames, object=True).pop()
	primes_per_second = sr / highest_prime

	return list(reader.read(int(math.floor(highest_prime * primes_per_second))).channel(1))


def main(*args, **kwargs):

	parser = argparse.ArgumentParser(description="Compare two audio files")
	parser.add_argument('-f1', dest="filename1", help="path to first file", type=file)
	parser.add_argument('-f2', dest="filename2", help="path to second file", type=file)
	args = parser.parse_args()
	filename = args.filename1
	filename2 = args.filename2
	if not args.filename1:
		filename = raw_input("Please enter a filename: ")
		filename = open(filename.replace('\\', ''))
	if not args.filename2:
		filename2 = raw_input("Please enter filname for comparison: ")
		filename2 = open(filename2.replace('\\', ''))
	array1 = get_frames(filename)
	array2 = get_frames(filename2)
	filename.close()
	filename2.close()
	count = 0
	for idx, val in enumerate(array1):
		if val == array2[idx]:
			count += 1

	print "Number of matching frames in first second of play: %d" % count

if __name__  == '__main__':
	main()
