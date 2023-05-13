from Bio import SeqIO
import random
genome_file = 'C:/Users/АлександрКондратюк/PycharmProjects/pythonProject18/GRCh38_latest_genomic.fna'

num_sequences = 100
sequence_length = 100

#output_file = 'C:/Users/АлександрКондратюк/PycharmProjects/pythonProject18'

genome_sequences = list(SeqIO.parse(genome_file, "fasta"))

random_sequences = random.sample(genome_sequences, num_sequences)

seq_records = [SeqIO.SeqRecord(seq.seq[:sequence_length], id=seq.id, description="") for seq in random_sequences]

with open("random_sequences.fasta", "w") as output_file:
    SeqIO.write(seq_records, output_file, "fasta")





