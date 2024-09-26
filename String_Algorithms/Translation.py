#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#Return: The protein string encoded by s.

# Codon dictionary mapping RNA codons to amino acids
codon_dict = {
    'UUU': 'F', 'UUC': 'F',  # Phenylalanine
    'UUA': 'L', 'UUG': 'L',  # Leucine
    'CUU': 'L', 'CUC': 'L',  # Leucine
    'CUA': 'L', 'CUG': 'L',  # Leucine
    'AUU': 'I', 'AUC': 'I',  # Isoleucine
    'AUA': 'I',              # Isoleucine
    'AUG': 'M',              # Methionine (start codon)
    'GUU': 'V', 'GUC': 'V',  # Valine
    'GUA': 'V', 'GUG': 'V',  # Valine
    'UCU': 'S', 'UCC': 'S',  # Serine
    'UCA': 'S', 'UCG': 'S',  # Serine
    'CCU': 'P', 'CCC': 'P',  # Proline
    'CCA': 'P', 'CCG': 'P',  # Proline
    'ACU': 'T', 'ACC': 'T',  # Threonine
    'ACA': 'T', 'ACG': 'T',  # Threonine
    'GCU': 'A', 'GCC': 'A',  # Alanine
    'GCA': 'A', 'GCG': 'A',  # Alanine
    'UAU': 'Y', 'UAC': 'Y',  # Tyrosine
    'UAA': '*',              # Stop codon
    'UAG': '*',              # Stop codon
    'CAU': 'H', 'CAC': 'H',  # Histidine
    'CAA': 'Q', 'CAG': 'Q',  # Glutamine
    'AAU': 'N', 'AAC': 'N',  # Asparagine
    'AAA': 'K',              # Lysine
    'AAG': 'K',              # Lysine
    'GAU': 'D', 'GAC': 'D',  # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',  # Glutamic Acid
    'UGU': 'C', 'UGC': 'C',  # Cysteine
    'UGA': '*',              # Stop codon
    'UGG': 'W',              # Tryptophan
    'CGU': 'R', 'CGC': 'R',  # Arginine
    'CGA': 'R', 'CGG': 'R',  # Arginine
    'AGU': 'S', 'AGC': 'S',  # Serine
    'AGA': 'R',              # Arginine
    'AGG': 'R',              # Arginine
    'GGU': 'G', 'GGC': 'G',  # Glycine
    'GGA': 'G', 'GGG': 'G',  # Glycine
}

def translate(rna_seq):
    return ''.join([codon_dict[rna_seq[i:i+3]] for i in range(0, len(rna_seq), 3)][:-1]) # The stop codon is ignored


rna_file = "data/translation.txt"

with open(rna_file, 'r') as f:
    rna_seq = f.readline().strip()

print(translate(rna_seq))



