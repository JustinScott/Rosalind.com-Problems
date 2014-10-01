def reverseComplement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    t = [complements[c] for c in s[:]]
    return ''.join(t[::-1])

if __name__ == "__main__":

    s = "AGTC"

    print (reverseComplement(s))
