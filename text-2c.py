AA_DA_MAP = {
    'G': 21, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
    'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


def mol_mass(sseq):
    mass_list = []
    for seq in sseq:
        mass = 0
        for aa in seq:
            mass = mass + AA_DA_MAP[aa]
        mass_list.append(mass)
    return mass_list


def sub_seq(ref, data_len):
    sseq = []
    for i in range(1, data_len):
        for j in range(0, data_len):
            sseq.append(ref[j:j + i])
    return sseq


if __name__ == '__main__':
    data = open("D:/net dlz/rosalind_test.txt").read().rstrip('\n')
    ref = ''.join([data, data])    #linear -> circular

    sseq = sub_seq(ref, len(data)) #find all subsequences
    sseq.append(data)              #add full peptide
    sseq.append('')                #add zero

    mm = mol_mass(sseq)            #calc weights for each subsequence
    mm.sort()

    #mm now contains the theoretical spectrum for the peptide 'ref'
    for weight in mm:
        print(weight, end=' ')


