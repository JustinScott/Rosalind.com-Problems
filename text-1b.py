def rev_comp(ref):
    c = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([c[x] for x in ref][::-1])


if __name__ == '__main__':
    f =open('D:/net dlz/dataset_3_2.txt').read().splitlines()
    print(rev_comp(''.join(f[:])))