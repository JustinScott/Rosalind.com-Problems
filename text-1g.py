def distance(s, t, err):
    count = 0;
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
            if count > err:
                return True
    return False


def approx_pattern(patterns, ref, err):
    match = {}
    for i in range(len(ref) - k_len + 1):
        for pattern in patterns:
            count = 0
            for j in range(len(pattern)):
                if pattern[j] != ref[i+j]:
                    count += 1
                    if count > err:
                        break
                #if distance(pattern, ref[i:i+len(pattern)], err):
                #    continue
            else:
                match[pattern] = match.get(pattern, 0) + 1
    m = max(match.values())
    [print(k, end=' ') for k, v in match.items() if v == m]

dna = ['A', 'G', 'T', 'C']


def immediate_neighbors(pattern):
    neighborhood = set([pattern])
    for i in range(len(pattern)):
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
    for j in range(k):
        chunks = [ref[i:i+k] for i in range(j, len(ref), k)]
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
    return kmers


if __name__ == '__main__':
    import time
    data = open('D:/net dlz/dataset_9_7.txt').read().splitlines()
    vals = data[1].split(' ')
    k_len = int(vals[0])
    all_kmers = gen_kmers(data[0], k_len, int(vals[1]))
    approx_pattern(all_kmers, data[0], int(vals[1]))