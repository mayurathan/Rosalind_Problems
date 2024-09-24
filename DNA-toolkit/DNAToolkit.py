Nucleotides = ["A","C","G","T"]
DNA_ReverseComplelemt = {'A': 'T', 'C': "G", 'G': 'C', 'T':'A'}

def validateSequence(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return True

#####################
# String Algorithms #
#####################

# tally the frequency of each nucleotide in 
def countNucFrequency(dna_seq):
    freqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in dna_seq:
        freqDict[nuc] += 1
    return freqDict

# DNA -> RNA transcription
def transcription(dna_seq):
    return dna_seq.replace("T", "U")

# Returns reverse complement of a DNA sequence
def reverse_complement(dna_seq):
    return ''.join([DNA_ReverseComplelemt[n] for n in dna_seq])[::-1]




