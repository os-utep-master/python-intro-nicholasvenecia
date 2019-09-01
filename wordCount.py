import os, sys, re, string

inputFile = sys.argv[1]
outputFile = sys.argv[2]

stringText = open(inputFile, 'r').read().lower()
expressionList = re.findall(r'\b[a-z]{1,15}\b', stringText)

occurrences = {}
for word in expressionList:
    count = occurrences.get(word, 0)
    occurrences[word] = count + 1

sortedList = sorted(occurrences.keys())

with open(outputFile, 'w') as output:
    for words in sortedList:
        output.writelines("%s %d\n" % (words, occurrences[words]))
