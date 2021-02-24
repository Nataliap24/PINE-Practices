#Write a python program that automatically calculate the answer to this question:
#Which is the most frequent base in each gene?

import Seq0

GENE_FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G"]

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    c = 0
    for base in base_list:
        count = Seq0.seq_count_base(sequence, base)
        if count > c:
            c = count
            b = base
    print("Gene", gene, ": Most frequent base:", b)
