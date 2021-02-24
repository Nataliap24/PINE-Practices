# Implement the seq_complement(seq) function, that calculates a new sequence composed of the complement base of each of the original bases.
# The bases work in pairs. A and T are complement, as well as C and G. Therefore, the complement sequence of "ATTCG" is "TAAGC". It should be written in the Seq0.py file
#Desription: Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene.
# This fragment should be printed on the console. Then calculate the complement of this fragment by calling the seq_complement() function. Finally print it on the console

import Seq0
print("Gene U5:")
sequence = Seq0.seq_read_fasta("./Sequences/U5.txt")[0:20]
print("Frag:", sequence)
print("Rev:", Seq0.seq_complement(sequence))