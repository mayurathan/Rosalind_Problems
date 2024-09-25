# Hamming Distance

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

def hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        print("Length of two dna sequences must match")

    return sum(1 for i in range(len(dna1)) if dna1[i] != dna2[i])

dna_file = "data/hamming_distance.txt"

sequences = []
with open(dna_file, 'r') as f:
    for line in f:
        line = line.strip()
        sequences.append(line)

print(hamming_distance(sequences[0], sequences[1]))
