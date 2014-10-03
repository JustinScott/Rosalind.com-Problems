def trans():
    transition = transversion = 0
    for s, t in zip(dna[0], dna[1]):
        if s != t:
            if (s, t) in [('G', 'A'), ('A', 'G'), ('C', 'T'), ('T', 'C')]:
                transition += 1
            else:
                transversion += 1
    print(float(transition/transversion))


if __name__ == "__main__":
    data = open("D:/net dlz/rosalind_tran.txt").read().split('>')[1:]
    dna = [''.join(x.split('\n')[1:]) for x in data]
    trans()