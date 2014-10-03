def permute(num):
    if len(num) == 2:
        yield num
        num[0], num[1] = num[1], num[0]
        yield num
    else:
        for i in range(0, len(num)):
            # fix the first number and get the permutations of the rest of numbers
            for perm in permute(num[0:i] + num[i+1:len(num)]):
                yield [num[i]] + perm


if __name__ == "__main__":
    n = int(open("D:/net dlz/rosalind_test.txt").read().rstrip())
    l = [x for x in range(1,5+1)]
    count = 0
    for p in permute(l):
        count += 1
        print(' '.join([str(t) for t in p]).rstrip())

    print(count)