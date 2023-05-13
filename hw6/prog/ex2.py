sequence = "AGTATAGTTCAGTTGTTTTCCTGTGTGAAGTCTCTGTAGCATTGACTGAATGTATAAGGGGACGAAGAGACAGAAGCTTCCTAGCGTAAGAAACATACCA"
fragment_length = 100
output_file = "fragments.fasta"


with open(output_file, "w") as f:
    for i in range(len(sequence), 0, -1):
        fragment = sequence[:i]
        header = f">fragment_{i}\n"
        f.write(header)
        f.write(fragment)
        f.write("\n")
