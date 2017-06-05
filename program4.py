#4. Write a Python program to count the number of lines in a text file.

filename = "words.txt"
numLines = 0
numWords = 0
numChars = 0

# we are going to use for loop
with open (filename, 'r') as file:
	for line in file:
		#Let's create a file for words
		wordList = line.split()
		numLines += 1
		numWords += len(wordList)
		numChars += len(line)
print "Lines:%i\nWords:%i\nCharacters:%i\n" %(numLines,numWords,numChars)

'''output
[root@test python]# python program4.py
Lines:3
Words:11
Characters:59'''
