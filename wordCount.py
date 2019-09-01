import os
import sys
import re
import string

firstArg = sys.argv[1]
secondArg = sys.argv[2]

frequency = {}
document_text = open(firstArg, 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = sorted(frequency.keys())

with open(secondArg, 'w') as kevin:
    for words in frequency_list:
        kevin.writelines("%s %s\n" % (words, str(frequency[words])))
