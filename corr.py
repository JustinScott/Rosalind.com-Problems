def parse_fasta(s):
    dna = []
    entries = s.split('>')
    for entry in entries[1:]:
        dna.append(''.join(entry.split('\n')[1:]))
    return dna


def reverse_complement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    list = [complements[c] for c in reversed(s)]
    return ''.join(list)


def ham_dist(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count


def error_correct(list):
    corr = []
    for i in range(len(list)-1):
        flag = False
        for j in range(i+1, len(list)-1):
            if list[i] == list[j] or list[i] == reverse_complement(list[j]):
                flag = True
                list[j] = ''
        if flag:
            corr.append(list[i])
            list[i] = ''

    for snp in list:
        if snp == '':
            continue
        for good in corr:
            if ham_dist(snp, good) == 1 or ham_dist(snp, reverse_complement(good)) == 1:
                print(snp, '->', good)
    return list


if __name__ == "__main__":
    f = open("D:/net dlz/rosalind_test.txt").read().strip()
    l = parse_fasta(f)
    x = error_correct(l)
    print(x)