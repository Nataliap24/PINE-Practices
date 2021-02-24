# Create a program for counting the number of bases presented in a DNA sequence.
# The user introduces a sequence of letter representing the DNA chain. For example: CATGTAGACTAG.
# Our program should calculate the total length, and the number of bases that compound the sequence.
# In the previous example sequence, the output of our program should be like this:
# Introduce the sequence: CATGTAGACTAG
# Total length: 12
# A: 4
# C: 2
# T: 3
# G: 3
# Considerations: You must use a loop for counting the bases

def correct_sequence(dna):
    for e in dna:
        if e != "A" or e != "C" or e != "G" or e != "T":
            return False
    return True

def count_bases(dna):
    a, c, g, t = 0, 0, 0, 0
    for e in dna:
        if e == "A":
            a += 1
        elif e == "C":
            c += 1
        elif e == "G":
            g += 1
        elif e == "T":
            t += 1
    return a, c, g, t

dna = input("Enter a dna sequence")
if correct_sequence(dna):
    print("Total length:", len(dna))
    a, c, g, t = count_bases(dna)
    print("A:", a, "\n", "c:", c, "\n", "T:", t, "\n", "G:", g)
else:
    print("Not a valid dna sequence")