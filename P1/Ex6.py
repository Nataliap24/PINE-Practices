import Seq1

def print_result(i, sequence):
    print("Sequence" + str(i) + ": (Length: " + str(sequence.len()) + " ) " + str(sequence))
    print("Bases: ", sequence.count())

print("--- Exercise 6 ---")
# We create the test_sequences() in Seq1 (because we are continiuously uing the same 3 sequences)
list_sequences = list(Seq1.test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])