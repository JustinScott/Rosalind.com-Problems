from collections import Counter
from operator import itemgetter

AA_DA_MAP = {
    'G': 21,  'A': 71,  'S': 87,  'P': 97,
    'V': 99,  'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


def peptide_to_amino_weights(peptide):
    return '-'.join([str(AA_DA_MAP[aa]) for aa in peptide])


def peptide_mass(peptide):
    return sum([AA_DA_MAP[aa] for aa in peptide])


def gen_subsequences(ref, data_len):
    sseq = [ref]
    for i in range(1, data_len):
        for j in range(0, data_len - i + 1):
            sseq.append(ref[j:j + i])
    return sseq


def theoretical_spectrum(peptide):
    subseqs = gen_subsequences(peptide, len(peptide))
    spect = [peptide_mass(seq) for seq in subseqs]
    return spect


def cyclopeptide_sequence(N):
    slist = ['']
    leader_peptide = ''
    while len(slist) > 0:
        slist = branch(slist)
        bound(slist, leader_peptide)
        slist = cut(slist, N)
    return leader_peptide


def branch(peptides):
    return [peptide + aa for peptide in peptides for aa in AA_DA_MAP.keys()]


def bound(slist, leader_peptide):
    for peptide in slist[:]:
        if peptide_mass(peptide) == parent_mass:
            if score(peptide) > score(leader_peptide):
                leader_peptide = peptide
        elif peptide_mass(peptide) > parent_mass:
            slist.remove(peptide)


def cut(slist, N):
    cutoff_map = {}
    for peptide in slist:
        cutoff_map[peptide] = score(peptide)
    t = sorted(cutoff_map.items(), key=itemgetter(1), reverse=True)[:N]
    cutoff_map = dict(t)
    return cutoff_map.keys()


def score(peptide):
    t = Counter(theoretical_spectrum(peptide))
    e = Counter(experimental_spectrum)
    c = t - e
    return spectrum_score - sum(c.keys())


if __name__ == '__main__':
    data = open("D:/net dlz/rosalind_test.txt").read().split('\n')
    experimental_spectrum = [int(n) for n in data[1].rstrip().split(' ')]
    N = int(data[0])
    parent_mass = max(experimental_spectrum)
    spectrum_score = len(experimental_spectrum)
    match = cyclopeptide_sequence(N)
    weights = peptide_to_amino_weights(match)

    for weight in weights:
        print(weight, end=' ')