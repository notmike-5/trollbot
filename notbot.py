###
##
# notmike bot
# MIT License, 2019
#
# notmike bot should: 
#		just say random things
# 		learn what others say.
#		Contributing Users: moriarty, M1, gmaxwell, rmah, latentprion, wintax, jim, Millenial
#
#
#Generate n-grams
#	1) count percent of the time word1 was followed by word 2, that is P(word1->word2)
#	2) Store in matrix... probability measured by relative occurence of words in static sample
#
#						[that's]	[Adam Smith]	[...]	[economy]	
#				[and]	  0.20			0.01		...		  0.30
#				 ...	  ...			...			...		  ...
#				 ...	  ... 			...			...	      ...
#				[why]	  0.1			0.0001		...		  0.005
#					
#		#some regex
#		awk '/<moriarty>.*/'					//pulls lines from user <moriarty>
#		sed -r 's/\[[^]]+\]\s+<moriarty>\s//g'	//remove timestamps and username
#		
#		awk '/<moriarty>.*/' \#\#econometrics.txt | sed -r 's/\[[^]]+\]\s+<moriarty>\s//g' > moriarty
#		
#		get a line
#		split on empty space
#		read each word, noting *some* punctuation (e.g. ',', '.', ';', ':', '?', '!', '(', ')', ... )
#			***determine appropriate responses
#		for each word if language[word][otherword] exists +1, otherwise create it and +1
#		sum across rows and divide each word[otherword] occurence by total occurances
#		repeat for each row			
#
#

from linecache import getline
from random import randint
import re
import time

def buildNGrams(filename):
	"""
	PRECONDITION: Given a textfile of newline character delimited strings
	POSTCONDITION: Returns nGrams, a list of lists (split strings)
	"""
	start = time.time()
	nGrams = []

	num_lines = sum(1 for line in open('language/%s' % filename))

	#pull each line, split it, append it to ngrams
	for i in range(num_lines):
		string = getline('language//%s' % filename, i)
		nGrams.append(string.split())

	#TODO: Close the file?
	end = time.time()
	print("\nnGrams built in %d seconds.\n" % (end-start))
	
	return nGrams

def getLinks(strings):
	"""
	PRECONDITION: Given a list of lists (nGrams)
	POSTCONDITION: Returns a list of strings (links)
	"""
	start = time.time()
	links = []

	for nGram in strings:
		if len(nGram) == 0:
			strings.remove(nGram)
		if len(nGram) == 1:
			if re.match('http.*', nGram[0]) is not None:
				index = strings.index(nGram)
				links.append(strings.pop(index))
				while strings.count(nGram) != 0:
					index = strings.index(nGram)
					strings.pop(index)
			else:
				strings.remove(nGram)
	end = time.time()
	print("Links cleaned in %d seconds.\n" % (end-start))
	return links

def buildMatrix(nGrams):
	pass

def __sumColumns(array):
	pass

#Main
nGrams = buildNGrams('language')

links = getLinks(nGrams)

print("\nnGrams:")
for i in range(5):
	print(nGrams[i])
print("\nLinks:")
for i in range(5):
	print(links[i])
