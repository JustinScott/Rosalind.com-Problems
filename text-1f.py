def distance(s, t):
    return sum([1 for x, y in zip(s, t) if x != y])


def approx_pattern(pattern, ref, err):
    for i in range(len(ref) - len(pattern) + 1):
        if distance(pattern, ref[i:i+len(pattern)]) > err:
            continue
        print(i, end=' ')


if __name__ == '__main__':
    data = open('D:/net dlz/dataset_9_4.txt').read().splitlines()
    #approx_pattern(data[0], data[1], int(data[2]))

    q = 'ATCAA'
    r = 'GATCAGTAGGAGTAAGCAGACTTCTATATCTATTTTCATGGCTTACAGTCCATTCACGGGGACCATCGGCAACGTCGTCTGACACACCGCTTTCACCGTATCAACCGGGCACTTTGCAAGATACGATTTCCGCACAGTCTACTACGCGTTCGGCCAGATCTTAACTTATCTTGTAATGTCCCTCATGCAGAAGGTTTGTCGCTCTAACAGCAAAGATCACAGTCTCAACCGATAGTTTATTTCCGCTAAATCATGCGGGTTGCCAGGGCCGAGCAGTGTAAACAACGTCTGGGATCAGTCGTCATGGGCGGTAACATTCCTAACGTGCGTGTGTAGTTCGCCGACGGGGC'
    approx_pattern(q, r, 2)