import Seq1

def print_result(i, sequence):
    print("Sequence" + str(i) + ": (Length: " + str(sequence.len()) + " ) " + str(sequence))
    print("Bases: ", sequence.count())
    print("Rev: ", sequence.reverse())
    print("Comp: ", sequence.complement())

print("--- Exercise 8 ---")
# We create the test sequences
list_sequences = list(Seq1.test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])