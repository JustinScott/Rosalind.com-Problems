def clump(ref, k, L, t):
    s = set()
    for i in range(0, len(ref)):
        chunks = [ref[j:j+k] for j in range(i, i+L)]
        m = {}
        for chunk in chunks:
            if len(chunk) != k:
                continue
            m[chunk] = m.get(chunk, 0) + 1
        [s.add(k) for k, v in m.items() if v == t]
    print(' '.join([x for x in s]))

if __name__ == '__main__':
    f =open('D:/net dlz/rosalind_1d.txt').read().splitlines()
    l = f[1].split(' ')
    clump(f[0], int(l[0]), int(l[1]), int(l[2]))
