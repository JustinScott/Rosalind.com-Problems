def parse_fasta(file):
    data = []
    list = file.split('>')[1:]
    for entry in list:
        data.append(''.join(entry.split('\n')[1:]))
    return data

def build_contig(parts):
    contig = parts[0]
    del parts[0]
    while len(parts) > 0:
        for part in parts:
            p_len = int(len(part)/2)
            pos = contig.find(part[0:p_len])
            if pos > -1:
                contig += part[len(contig) - pos:]
                parts.remove(part)
                continue
            pos = contig.find(part[p_len:])
            if pos > -1:
                contig = part[0:p_len-pos] + contig
                parts.remove(part)
                continue
    return contig

if __name__ == "__main__":
    f = open("D:/net dlz/rosalind_long.txt").read().strip()
    m = parse_fasta(f)
    c = build_contig(m)
    print(c)