#!/usr/bin/python

def common_substring(ref, strings):
    substring = ''
    for i in range(len(ref)):
        for j in range(i + 1, len(ref)):
            if all(string.find(ref[i:j]) > 0 for string in strings):
                substring = max(ref[i:j], substring, key=len)
    print(substring)


if __name__ == "__main__":
    data = open("D:/net dlz/rosalind_lcsm.txt").read().split('>')[1:]
    dna = [''.join(s.split('\n')[1:]) for s in data]
    common_substring(dna[0], dna[1:])