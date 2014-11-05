def subseq(pattern, ref):
    pos = 0
    while True:
        x = ref.find(pattern, pos)
        if x == -1:
            break
        else:
            pos = (x + 1)
            print(x, end=' ')



if __name__ == '__main__':
    data = open("D:/net dlz/Vibrio_cholerae.txt").read().split('\n')
    subseq(data[0], data[1])