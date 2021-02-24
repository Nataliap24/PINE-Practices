#EXERCISE 3
#Have a look at the dna files that you have downloaded in the previous exercise.
#Notice that they consist of two parts: a head an a body.
#The first line is the head, which starts with the '>' symbol.
#The following lines are the body and contains the sequence of nucleotides

from pathlib import Path
FILENAME = "RNU6_269P.txt"
text = Path(FILENAME).read_text()
lines = text.split("\n")
print (lines[0])

#some other prosibilities are:
# from pathlib import Path
#FILENAME = "RNU6_269P.txt"
#text = Path(FILENAME).open()
#lines = text.readline("\n")
#print (lines)

#from pathlib import Path
#FILENAME = "RNU6_269P.txt"
#text = Path(FILENAME).read_text()
#list_of_lines = text.splitlines()
#print (list_of_lines[0])