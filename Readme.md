Objective:
* takes as input the name of an input file and output file.
`$ python wordCount.py input.txt output.txt`
* is case-insensitive and keeps track of the total the number of times each word occurs in the text file while excluding white space and punctuation
* will print out to the output file (overwriting if it exists) the list of
  words sorted in descending order with their respective totals
  separated by a space, one word per line
* The re regular expression library and python dictionaries should be
used in your program. 

Running the code: 
To run wordCount: 
`$ python wordCountTest.py declaration.txt myOutput.txt`
To run wordCountTest: 
`$ python wordCountTest.py declaration.txt myOutput.txt declarationKey.txt`

Additional: 
Code written by Nicholas Venecia
Monitored and modified by Kevin Apodaca & Jaime Salas
* Kevin helped me understand and create the loop for the creation and writing to the output file.
* Jaime helped me understand the libraries and their uses.

Citations:
For sorting:
https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
For frequency:
https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965