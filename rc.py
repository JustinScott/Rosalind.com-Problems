def reverse_complement(s):
    complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    
    sc = reversed(s)
    sc = [complements[c] for c in sc]

    return ''.join(sc)


if __name__ == "__main__":

    small_dataset = "AAAACCCGGT"
    large_dataset = "GGTTGTCTTCACGACAACACCGCGCTGGCCAAGGTATTAAATAGGCGCATCACTGCTTCTCCCATGACATTGAAAAGGTTAACTTCCCCCATCCAACGTCAGTCTCCATTCTTTCAGTCGGGGGCAAATATGACCGGAGTTAAAGGACTCGAGCTATTGCAGAGCCACGGACGAGAGCAATTCACCAGAGCATAGCAAAAGTGCCGGCCGGCCTACGACCCGGAGACCGTGAAGTTGCGTCCCATTGCTGTTGCATTACAACCGCTCGCGAACGCATCAGTTGGTATATATATCTAAAAGCGTGGCGTGGCCTTGGTACTATTCGGAGAGATCCTAGTTATGCATGAGCAAGCTCGCCGTACGGGTCTGCCACGGTGGAGTTGAGTTTGTAGGCGATAGCCTAGCCGACGGGCTGACTGCGCCAAGAGACTTTCTCCTGATTGAGCTTATGATTGAAAGGCAACGACACAATCATATCGCCGGCGAGTAGACGTCTACTAAAGTTACAGTATTATTTAGCGGCTGAGGAGTTCACACCCTGTCCCAGGTGCGGACAATACTGCTATCTAGGGGCACATGGGTGATGGCATCGGACCGTATTGGATGGGAGGAAATTGGTTCCTTTAGACTAAAGGGTCGTTTCAGCGACAAATATTCAACGTCCCTCTTTTCGGATTTCATTTGCTCATGCAGATCGTGACTACTTACCTGCGACCCGGTAGACATGTGAAGGCTGTTTGTCTAATATCCTTGCATGAGGGTCGACGTATATTGGTCTACCAGGTTCAAGACAGCGGACTATGTATAATCTTCTGGTGTTCCATTAACTCACCCTCAGACCCGACGAAATCCAGCCAACCCTGGGAACTGATATCCCCACAAAATTTCTC"

    print reverse_complement(large_dataset)
