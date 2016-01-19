#	Kristján Hall 2016
#
#	password generator using a dictionary file
#	of known words
#
#

import sys
import random

def generateLineNumbers(num):
	return random.sample(range(1, 241820), num)


def pickWords(numbers):
	words = []
	fp = open("dict.txt")
	for i, word in enumerate(fp):
		if i in numbers:
			words.append(word.rstrip().replace("-", ""))
	fp.close()

	return words


def makePassword(numberOfWords=4):
	ns = generateLineNumbers(numberOfWords)
	words = pickWords(ns)
	return " ".join(words)


def main(args):

	try:
		count = int(args[0])
		if count > 0 and count < 10:
			password = makePassword(count)
			print("\nYour password is\n{0}\n{1}\n".format(len(password) * "=", password))
		else:
			print("Number of words must be between 1 and 10")

	except:
		print("Argument must be an integer")


if __name__ == "__main__":
	main(sys.argv[1:])