# Computing GC content

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

fasta_file = "data/fasta.txt"

# Dictionary to store id with a list of sequences
sequences = {}
current_sequence = []
current_id = None

with open(fasta_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            if current_id:
                sequences[current_id] = ''.join(current_sequence)
            current_id = line[1:]
            current_sequence = []
        else:
            current_sequence.append(line)

# Store the last sequence
sequences[current_id] = ''.join(current_sequence)

mostGC_ratio = 0

mostGC_ID = None

for seq_id, sequence in sequences.items():
    gc_count = 0
    seq_length = len(sequence)
    for c in sequence:
        if c == 'G' or c == 'C':
            gc_count += 1
    gc_ratio = float(gc_count) / float(seq_length) * 100
    if gc_ratio > mostGC_ratio:
        mostGC_ratio = gc_ratio
        mostGC_ID = seq_id

print(f"{mostGC_ID}\n{mostGC_ratio}")



