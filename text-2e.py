AA_DA_MAP = {
    'G': 21,  'A': 71,  'S': 87,  'P': 97,
    'V': 99,  'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


def peptides_to_amino_weights(p_list):
    weight_set = set()
    for peptide in p_list:
        weight_string = '-'.join([str(AA_DA_MAP[aa]) for aa in peptide])
        weight_set.add(weight_string)
    return weight_set


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


def cyclopeptide_sequence():
    match_list = []
    slist = [aa for aa in AA_DA_MAP.keys()]
    while len(slist) > 0:
        bound(slist, match_list)
        slist = branch(slist)
    return match_list


def branch(slist):
    extended_list = []
    for peptide in slist:
        for aa in AA_DA_MAP.keys():
            extended_list.append(''.join([peptide, aa]))
    return extended_list


def bound(slist, match_list):
    for peptide in slist[:]:
        if consistent(peptide):
            if peptide_mass(peptide) == parent_mass:
                slist.remove(peptide)
                match_list.append(peptide)
        else:
            slist.remove(peptide)


def consistent(peptide):
    experimental_spectrum = list(spectrum) #make a copy so it can be modified
    t_spectrum = theoretical_spectrum(peptide)
    for mass in t_spectrum:
        if mass in experimental_spectrum:
            #removing it to ensure that duplicate values are matched correctly
            experimental_spectrum.remove(mass)
        else:
            # mass not found, break and return false
            break
    else:
        # loop fell through, so all masses were in spectrum
        return True

    return False


if __name__ == '__main__':
    spectrum = open("D:/net dlz/rosalind_2e.txt").read().rstrip('\n')
    spectrum = [int(n) for n in spectrum.split(' ')]
    parent_mass = max(spectrum)
    match = cyclopeptide_sequence()
    weights = peptides_to_amino_weights(match)

    for weight in weights:
        print(weight, end=' ')