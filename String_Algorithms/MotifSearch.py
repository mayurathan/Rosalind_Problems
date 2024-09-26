# Finding motif in DNA

#Given: Two DNA strings s and t (each of length at most 1 kbp).
#Return: All locations of t as a substring of s.

def getIndex(dna_seq, motif):
    motif_length = len(motif)
    indexes = [i + 1 for i in range(len(dna_seq)) if dna_seq.startswith(motif, i)]
    return indexes

data_file = "data/motifsearch.txt"

with open(data_file, 'r') as f:
    file_content = f.readlines()

dna_seq = file_content[0].strip()
motif = file_content[1].strip()

#print(f"DNA Seuqnce: {dna_seq}")
#print(f"Motif: {motif}")

motif_location = getIndex(dna_seq, motif)
motif_location = ' '.join(map(str, motif_location)) # Convert list to string of location

print(motif_location)
