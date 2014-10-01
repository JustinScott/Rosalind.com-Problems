def reverse_complement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    list = [complements[c] for c in reversed(s)]
    return ''.join(list)

def restriction_site(dna):
    sites = {}
    for i in range(len(dna)):
        for j in range(4,13,2):
            s = dna[i:i+j]
            t = reverse_complement(s)
            if s == t and i+j <= len(dna):
              sites[i+1] = len(s)
    return sites

if __name__ == "__main__":
    s = "TCAATGCATGCGGGTCTATATGCAT"
    t = open('D:/net dlz/rosalind_revp.txt').read().splitlines()
    t = ''.join(t[1:])

    x = restriction_site(t)

    for k,v in x.items():
        print(k, v)