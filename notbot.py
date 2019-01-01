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

def makeNGrams(file):
	nGrams = []

	num_lines = sum(1 for line in open('language/%s' % file))

	for line in range(num_lines):
		string = getline('language//%s' % file, line)
		nGrams.append(string.split())

	return nGrams

def getLinks(list):
	links = []

	for nGram in list:
		#remove all singles
		if len(nGram) == 1:
			if re.match('http.*', nGram[0]) is not None:
				links.append(nGram.pop(0))	

	return links

#Main
test = makeNGrams('language')
links = getLinks(test)

for link in links:
	print(link)

for nGram in test:
	print(nGram)