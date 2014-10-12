def lgis(n, perm):
    lens = [1]
    pred = ['-']
    L = 1

    for i in range(1, len(perm)):
        lo = 1
        hi = L
        while(lo <= hi):
            mid = (hi + lo)/2
            if perm[lens[mid]] < perm[i]:
                lo = mid + 1
            else:
                hi = mid - 1


if __name__ == '__main__':
    data = open("D:/net dlz/rosalind_test.txt").read().splitlines()
    perm = ''.join(data[1:]).split()
    lgis(data[0], perm)