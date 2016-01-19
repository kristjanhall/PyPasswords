import random
import sys

class passphrase:

	def __init__(self):
		pass
		self.Lcount = self.getWordCount(open("l.txt"))
		self.Ncount = self.getWordCount(open("n.txt"))
		self.Scount = self.getWordCount(open("s.txt"))

	def getWordCount(self, fp):
		for i, word in enumerate(fp):
			pass
		return i

	def getLineFromFile(self, n, f):
		with open(f) as fp:
			for i, word in enumerate(fp):
				if i == n:
					return word.rstrip().replace("-", "")


	def generateLineNumber(self, n):
		return random.sample(range(1, n), 1)


	def pickL(self):
		n = self.generateLineNumber(self.Lcount)
		return self.getLineFromFile(n[0], "l.txt")


	def pickS(self):
		n = self.generateLineNumber(self.Scount)
		return self.getLineFromFile(n[0], "s.txt")


	def pickN(self):
		n = self.generateLineNumber(self.Ncount)
		return self.getLineFromFile(n[0], "n.txt")


	def makePassPhrase(self):
		phrase = [
			self.pickL(),
			self.pickN(),
			self.pickS(),
			self.pickN()
		]
		phrase = " ".join(phrase)
		return phrase



def main():
	pp = passphrase()
	password =pp.makePassPhrase()
	print("\n{0}".format("=" * len(password)))
	print(password)
	print("{0}\n".format("=" * len(password)))


if __name__ == "__main__":
	main()