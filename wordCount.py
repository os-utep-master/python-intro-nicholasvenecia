# Created and written by Nicholas Venecia on August 31, 2019.
# Monitored & modified by Kevin Apodaca & Jaime Salas.

import os, sys, re, string

# Arguments made in the terminal following call to wordCount.
# inputFile will be the name of the file we want to read from.
# outputFile will be the name of the file we want to write to.
inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Reaf from inputFile and save the file as a string called stringText
stringText = open(inputFile, 'r').read().lower()
# Separate each word in stringText according to the expression given.
# This expression should only accept words with a length
# no less than 1 character and no greater than 15 characters.
expressionList = re.findall(r'\b[a-z]{1,15}\b', stringText)

# Create an empty dictionary called occurrences. This is where all
# the unique words will be stored and each occurrences of the word
# will be counted and added to the value of the word.
occurrences = {}
for word in expressionList:
    count = occurrences.get(word, 0)
    occurrences[word] = count + 1

# Sort all the keys in the dictionary occurrences in alphavetical order
# and store them into a new dictionary called sortedList.
sortedList = sorted(occurrences.keys())

# Create a new text file called outputFile and write all the contents of
# sorted list to the file.
with open(outputFile, 'w') as output:
    for words in sortedList:
        output.writelines("%s %d\n" % (words, occurrences[words]))
