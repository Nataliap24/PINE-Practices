#Implement the generate_seqs() function

class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def generate_seqs(pattern, number):
    list_seq = []
    str_pattern = ""
    for i in range(0, number):
        str_pattern += pattern
        list_seq.append(Seq(str_pattern))
        if len(list_seq) == number:
            return list_seq

def print_seqs(list_seq):
    for element in list_seq:
        print("Sequence " + str(list_seq.index(element)) + ": (Length:", element.len(), ")",  element)


#Main programme
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)
print("List 1:")
print_seqs(seq_list1)

print("List 2:")
print_seqs(seq_list2)