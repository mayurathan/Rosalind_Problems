# Consensus and Profile

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

def readFasta(file_path):
    with open(file_path, 'r') as f:
        sequences = []
        current_seq = []
        for line in f:
            if line.startswith('>'):
                if current_seq:
                    sequences.append(''.join(current_seq))
                    current_seq = []
            else:
                current_seq.append(line.strip())
        sequences.append(''.join(current_seq))
    return sequences

def profile_and_concensus(sequence_list):
    sequence_length = len(sequence_list[0])
    profile = {
            'A':[0] * sequence_length,
            'C':[0] * sequence_length,
            'G':[0] * sequence_length,
            'T':[0] * sequence_length
            }

    for seq in sequence_list:
        for index, nuc in enumerate(seq):
            profile[nuc][index] += 1

    consensus = []

    for i in range(sequence_length):
        consensus_nucleotide = "A"
        consensus_count = profile[consensus_nucleotide][i]

        for nuc in "CGT":
            if profile[nuc][i] > consensus_count:
                consensus_nucleotide = nuc
                consensus_count = profile[nuc][i]

        consensus.append(consensus_nucleotide)

    return ''.join(consensus), profile

def print_profile(profile):
    for nucleotide in 'ACGT':
        print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")

fasta_file = "data/consensus_sequence.txt"

sequences = readFasta(fasta_file)
consensus, profile = profile_and_concensus(sequences)
print(consensus)
print_profile(profile)
