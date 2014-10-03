def parse_fasta(s):
    return [x for x in s if x[0] != '>']


def reverse_complement(s):
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([complements[c] for c in reversed(s)])


def ham_dist(s, t):
    return len([x for x, y in zip(s, t) if x != y])


def error_correct(data):
    good = [reverse_complement(x) for x in data] + data
    good = set([x for x in good if good.count(x) > 1])
    bad = set(data) - good

    for b in bad:
        for g in good:
            if ham_dist(b, g) == 1:
                print(b, '->', g, sep='')


if __name__ == "__main__":
    f = open("D:/net dlz/rosalind_test.txt").read().splitlines()
    l = parse_fasta(f)
    error_correct(l)