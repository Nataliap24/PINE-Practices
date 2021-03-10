#We need to develop the function print_seqs(seq_list) that receives a list of sequences and prints their number in the list, their length and the sequence itself
class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

#Main programme
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for element in seq_list:
    print("Sequence", seq_list.index(element), "-->", "Length:", element.len(), element)