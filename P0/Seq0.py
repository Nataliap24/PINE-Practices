from pathlib import Path

#for Ex1
def seq_ping():
    print("Ok")

#For Ex2
def seq_read_fasta(filename):
    sequence = Path(filename).read_text()
    sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
    return sequence

#For Ex3
def seq_len(seq):
    return len(seq)

#For Ex4
def seq_count_base(seq, base):
    return seq.count(base)

#For Ex5
def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict

#For Ex6
def seq_reverse(seq):
    return seq[::-1]

#Foe Ex7
def seq_complement(seq):
    new_seq = ""
    for base in seq:
        if base == "A":
            new_seq += "T"
        elif base == "T":
            new_seq += "A"
        elif base == "C":
            new_seq += "G"
        elif base == "G":
            new_seq += "C"
    return new_seq




