from Seq1 import Seq
GENE_FOLDER = "../P0/Sequences/"

def gene(argument): #argument = gene name
    #print_colored("GENE", "yellow")
    seq = Seq()
    seq.read_fasta(GENE_FOLDER + argument + ".txt")
    #complete_seq = str(seq.read_fasta(GENE_FOLDER + argument + ".txt"))
    #cs.send(complete_seq.encode())
    #print(complete_seq)
    print(seq)

print(gene("U5"))