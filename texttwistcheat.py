#!/usr/bin/env Python
# Adam R. Rivers 
import argparse
import cPickle as pickle

parser = argparse.ArgumentParser(description='texttwistcheat.py: a script to solve the letter game TextTwist')
parser.add_argument('-l','--lett', help='The letters given',required=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d','--dict', help='The text dictionary file')
group.add_argument('-u','--usepickle', help='The pickle file of the dictionary')
parser.add_argument('-s','--savepickle', help='the path to save the Python pickle dictionary file')
args = parser.parse_args()

#Functions
def parsedict(filename):
	"""Returns a dictionary with words and vectors of letter counts"""
	with open(filename,'r') as dict:
		vdict = {}
		for line in dict:
			vect =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			for letter in line.strip().lower():
				if letter == 'a':
					vect[0] += 1
				elif letter == 'b':
					vect[1] += 1
				elif letter == 'c':
					vect[2] += 1
				elif letter == 'd':
					vect[3] += 1
				elif letter == 'e':
					vect[4] += 1
				elif letter == 'f':
					vect[5] += 1
				elif letter == 'g':
					vect[6] += 1
				elif letter == 'h':
					vect[7] += 1
				elif letter == 'i':
					vect[8] += 1
				elif letter == 'j':
					vect[9] += 1
				elif letter == 'k':
					vect[10] += 1
				elif letter == 'l':
					vect[11] += 1
				elif letter == 'm':
					vect[12] += 1
				elif letter == 'n':
					vect[13] += 1
				elif letter == 'o':
					vect[14] += 1
				elif letter == 'p':
					vect[15] += 1
				elif letter == 'q':
					vect[16] += 1
				elif letter == 'r':
					vect[17] += 1
				elif letter == 's':
					vect[18] += 1
				elif letter == 't':
					vect[19] += 1
				elif letter == 'u':
					vect[20] += 1
				elif letter == 'v':
					vect[21] += 1
				elif letter == 'w':
					vect[22] += 1
				elif letter == 'x':
					vect[23] += 1
				elif letter == 'y':
					vect[24] += 1
				elif letter == 'z':
					vect[25] += 1
				else:
					pass
				vdict[line.strip().lower()] = vect
	return vdict
				
def inputvect(letters):
	"""Returns a vector with the count of letters in the search string"""
	vect =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	
	for letter in letters.lower():
		if letter == 'a':
			vect[0] += 1
		elif letter == 'b':
			vect[1] += 1
		elif letter == 'c':
			vect[2] += 1
		elif letter == 'd':
			vect[3] += 1
		elif letter == 'e':
			vect[4] += 1
		elif letter == 'f':
			vect[5] += 1
		elif letter == 'g':
			vect[6] += 1
		elif letter == 'h':
			vect[7] += 1
		elif letter == 'i':
			vect[8] += 1
		elif letter == 'j':
			vect[9] += 1
		elif letter == 'k':
			vect[10] += 1
		elif letter == 'l':
			vect[11] += 1
		elif letter == 'm':
			vect[12] += 1
		elif letter == 'n':
			vect[13] += 1
		elif letter == 'o':
			vect[14] += 1
		elif letter == 'p':
			vect[15] += 1
		elif letter == 'q':
			vect[16] += 1
		elif letter == 'r':
			vect[17] += 1
		elif letter == 's':
			vect[18] += 1
		elif letter == 't':
			vect[19] += 1
		elif letter == 'u':
			vect[20] += 1
		elif letter == 'v':
			vect[21] += 1
		elif letter == 'w':
			vect[22] += 1
		elif letter == 'x':
			vect[23] += 1
		elif letter == 'y':
			vect[24] += 1
		elif letter == 'z':
			vect[25] += 1
		else:
			pass
	return vect
	
def findwords(letters, dictionary):
	"""Returns a list ordered from the largest words to smallest words that can be made from the input letters"""
	matches = [] # create an empty list
	for key,item in dictionary.iteritems():
		write = True
		for i in range(26):
			if letters[i] - item[i] < 0:
				write = False	
		if len(key) >= 3 and write == True: # if enough letters are present and the work is 3 characters or longer write to list
			matches.append(key)
	matches.sort(key=len)
	matches.reverse()
	return matches
			
def main():		
	print("Loading dictionary")
	if args.usepickle:
		with open(args.usepickle, 'rb') as op:
			dictionary = pickle.load(op)
	elif args.dict:
		dictionary = parsedict(args.dict)
		if args.savepickle:
			with open(args.savepickle, 'wb') as sp:
				pickle.dump(dictionary,sp)
	else:
		raise IOError('No input dictionary was given. Please provide a dictionary as a text file or a pickle file')

	print("Examining the letters you gave")
	letters = inputvect(args.lett)

	print("Finding matches")
	answer = findwords(letters,dictionary)

	print("Matching words are:")
	print(answer)

if __name__ == "__main__":
    main()