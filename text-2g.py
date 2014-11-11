from collections import Counter
from operator import itemgetter


def convolution(spectrum):
    conv_list = [num1 - num2 for num1 in  spectrum for num2 in spectrum if num1 - num2 > 0]
    conv_map = Counter(conv_list)
    sorted_conv_list = sorted(conv_map.items(), key=itemgetter(1), reverse=True)
    return [tup[0] for tup in sorted_conv_list for i in range(tup[1])]


if __name__ == '__main__':
    spectrum = open('D:/net dlz/rosalind_2g.txt').read().rstrip('\n')
    spectrum = [int(num) for num in spectrum.split(' ')]
    conv = convolution(spectrum)
    for num in conv:
        print(num, end=' ')