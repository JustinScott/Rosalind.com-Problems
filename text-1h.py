def distance(s, t, err):
    count = 0;
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
            if count > err:
                return True
    return False

from collections import defaultdict


def approx_pattern(patterns, ref, err):
    match = defaultdict(int)
    for i in range(len(ref) - k_len + 1):
        for pattern in patterns:
            count = 0
            for j in range(k_len):
                if pattern[j] != ref[i+j]:
                    count += 1
                    if count > err:
                        break
            else:
                match[pattern] += 1
    m = max(match.values())
    [print(k, end=' ') for k, v in match.items() if v == m]

dna = ['A', 'G', 'T', 'C']


def immediate_neighbors(pattern):
    neighborhood = set([pattern])
    for i in range(k_len):
        for letter in dna:
            neighborhood.add(''.join([pattern[:i] + letter + pattern[i+1:]]))
    return neighborhood

def neighbors(pattern, d):
    neighborhood = set([pattern])
    for i in range(d):
        for x in neighborhood:
            neighborhood = neighborhood.union(immediate_neighbors(x))
    return neighborhood

def get_kmers(ref, k):
    map = {}
    r_len = len(ref)
    for j in range(k):
        chunks = [ref[i:i+k] for i in range(j, r_len, k)]
        for chunk in chunks:
            if len(chunk) != k:
                continue
            map[chunk] = map.get(chunk, 0) + 1
    return map


def gen_kmers(ref, k, d):
    kmers = set()
    kmap = get_kmers(ref, k)
    for k in kmap.keys():
        kmers = kmers.union(neighbors(k, d))
    #rev = set()
    #for k in kmers:
    #    rev.add(rev_comp(k))
    #kmers.union(rev)
    return kmers


def rev_comp(ref):
    c = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([c[x] for x in ref][::-1])

    
if __name__ == '__main__':
    import time
    data = open('D:/net dlz/rosalind_1h.txt').read().splitlines()
    vals = data[1].split(' ')
    k_len = int(vals[0])
    start_time = time.time()
    all_kmers = gen_kmers(data[0], k_len, int(vals[1]))
    print('kmers gen time: ', time.time() - start_time)
    print("kmers length: ", len(all_kmers))
    start_time = time.time()
    approx_pattern(all_kmers, data[0], int(vals[1]))
    print('pattern time: ', time.time() - start_time)