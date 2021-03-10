from pathlib import Path
import termcolor

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

#For Ex7
def seq_complement(seq):
    dict_compl = {"A":"T", "C":"G", "G":"C", "T":"A"}
    new_seq = ""
    for base in seq:
        for key, value in dict_compl.items():
            if base == key:
                new_seq += value
    return new_seq

#For session6
class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        if self.is_valid_sequence():
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("Incorrect sequence detected")

    def is_valid_sequence(self):
        for b in self.strbases:
            if b != "A" and b != "C" and b != "G" and b != "T":
                return False
            return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ": (Length 3)" + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

#for ex3 session 6

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq


