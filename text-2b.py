DNA_CODON_PROTEIN_MAP = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def rev_comp(ref):
    c = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([c[x] for x in ref][::-1])


def translate(s):
    seq = [DNA_CODON_PROTEIN_MAP[s[i:i+3]] for i in range(0, len(s), 3)]
    return "".join(seq)


def orf(ref, aa_seq):
    seq_len = len(aa_seq) * 3
    for j in range(0, len(ref) - seq_len + 1):
        if aa_seq == translate(ref[j:j+seq_len]) or aa_seq == translate(rev_comp(ref[j:j+seq_len])):
            print(ref[j:j+seq_len])


if __name__ == "__main__":
    data = open("D:/net dlz/rosalind_2b.txt").read().splitlines()
    orf(data[0], data[1])