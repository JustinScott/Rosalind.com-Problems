def distance(string1, string2):
    return sum([1 for x, y in zip(string1, string2) if x != y])


def gen_kmers(k, d, ref):
    kmers = set()
    for i in range(0, d):
        for j in range(0, k):
            for aa in ['A', 'T', 'G', 'C']:
                if aa != ref[j]:
                    kmers.add(ref[0:j] + aa + ref[j+1:])
    return kmers


def motifenumeration(k, d, dna):
    for i in range(0, len(dna[0]) - k + 1):
        kmers = gen_kmers(k, d, dna[0][i:i+k])
        for kmer in kmers:
            for j in range(0, len(dna)):
                match = False
                for m in range(0, len(dna[j]) - k + 1):
                    if distance(kmer, dna[j][m:m+k]) == d:
                        match = True
                        break
                if not match:
                    break
            else:
                print(kmer)


def main():
    data = open('D:/net dlz/rosalind_test.txt').read().split('\n')
    k = data[0].split(' ')[0]
    d = data[0].split(' ')[1]
    motifenumeration(int(k), int(d), data[1:])


if __name__ == '__main__':
    main()