#Implement the seq_reverse(seq) function, that calculates the reverse of the given sequence.
#Imaging we have this sequence: "ATTCG". Its reverse is: "GCTTA". It should be written in the Seq0.py file
#Desription: Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene. This fragment should be printed on the console.
#Then calculate the reverse of this fragment by calling the seq_reverse() function. Finally print it on the console

import Seq0
print("Gene U5:")
sequence = Seq0.seq_read_fasta("./Sequences/U5.txt")[0:20]
print("Frag:", sequence)
print("Rev:", Seq0.seq_reverse(sequence))
