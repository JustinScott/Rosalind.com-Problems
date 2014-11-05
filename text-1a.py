def freq_k(ref, k):
    map = {}
    for j in range(k):
        chunks = [ref[i:i+k] for i in range(j, len(ref), k)]
        for chunk in chunks:
            if len(chunk) != k:
                continue
            map[chunk] = map.get(chunk, 0) + 1
    l = [k for k, v in map.items() if v == max(map.values())]
    for x in l:
        print(x, end=' ')

if __name__ == '__main__':
    f =open('D:/net dlz/dataset_2_9.txt').read().splitlines()
    freq_k(f[0], int(f[1]))