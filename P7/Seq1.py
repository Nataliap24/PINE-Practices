import termcolor
from pathlib import Path

class Seq:

    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases=NULL_SEQUENCE):
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.strbases = strbases
        else:
            self.strbases = strbases
            if self.is_valid_sequence():
                print("New sequence created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
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
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                else:
                    t += 1
            return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        dict_bases = {"A": a, "C": c, "G": g, "T": t}
        return dict_bases

    def percentage(self):
        count = self.count_bases()
        sum = count[0] + count[1] + count[2] + count[3]
        list_bases = ['a', 'c', 'g', 't']
        list_per = []
        for i in range(0, len(count)):
            per = str(round((count[i] * 100) / sum, 2))
            list_per.append(list_bases[i] + ': ' + str(count[i]) + '  --> ' + per + '%')
        return list_per

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                else:
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    def most_freq_base(self):
        dict_bases = self.count()
        return max(dict_bases, key=dict_bases.get)

def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid Sequence")
    return s1, s2, s3

