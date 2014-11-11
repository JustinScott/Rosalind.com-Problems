def distance(string1, string2):
    return sum([1 for x, y in zip(string1, string2) if x != y])


def gen_kmers(k, d, ref):
    kmers = set()
    kmers.add(ref)
    new = set()
    for i in range(0, d):
        for kmer in kmers.copy():
            for j in range(0, k):
                for aa in ['A', 'T', 'G', 'C']:
                    new.add(kmer[0:j] + aa + kmer[j+1:])
    return kmers


def motifenumeration(k, d, dna):
    out = set()
    for i in range(0, len(dna[0]) - k + 1):
        kmers = gen_kmers(k, d, dna[0][i:i+k])
        for kmer in kmers:
            for j in range(0, len(dna)):
                match = False
                for m in range(0, len(dna[j]) - k + 1):
                    if distance(kmer, dna[j][m:m+k]) <= d:
                        match = True
                        break
                if not match:
                    break
            else:
                out.add(kmer)
    return out


def main():
    data = open('D:/net dlz/rosalind_3a.txt').read().split('\n')
    k = data[0].split(' ')[0]
    d = data[0].split(' ')[1]
    kmers = motifenumeration(int(k), int(d), data[1:])
    for kmer in kmers:
        print(kmer, end=' ')


if __name__ == '__main__':
    main()