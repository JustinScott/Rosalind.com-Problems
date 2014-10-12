def motif(s, t):
    position = 0
    ndx = []
    for letter in t:
        position = s.find(letter, position) + 1
        ndx.append(position)
    for x in ndx:
        print(x, end = ' ')

if __name__ == "__main__":
    data = open("D:/net dlz/rosalind_sseq.txt").read().split('>')[1:]
    dna = [''.join(x.split('\n')[1:]) for x in data]
    motif(dna[0], dna[1])