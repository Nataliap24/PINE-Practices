

def correct_sequence(dna):
    for e in dna:
        if e != "A" and e != "C" and e != "G" and e != "T":
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

def read_from_file(filename):
    with open(filename, "r") as f:
        dna = f.read()
        dna = dna.replace("\n", "")
        return dna


dna = input("Enter a dna sequence")
if correct_sequence(dna):
    print("Total length:", len(dna))
    a, c, g, t = count_bases(dna)
    print("A:", a, "\n", "c:", c, "\n", "T:", t, "\n", "G:", g)
else:
    print("Not a valid dna sequence")