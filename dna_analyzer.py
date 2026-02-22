def read_fasta(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        sequence = ""
        for line in lines:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence.upper()
dna = read_fasta("C:/Users/tejas/AppData/Local/Programs/Python/Python313/dna/sequence.fasta")
length = len(dna)
print("Length:", length)
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
gc_content = ((g_count + c_count) / length) * 100
print("GC Content: {:.2f}%".format(gc_content))
complement = ""
for base in dna:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement += "G"

reverse_complement = complement[::-1]
print("Reverse Complement:", reverse_complement)
def read_fasta(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        sequence = ""
        for line in lines:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence.upper()
dna = read_fasta("C:/Users/tejas/AppData/Local/Programs/Python/Python313/dna/sequence.fasta")
start_positions = []

for i in range(len(dna)-2):
    codon = dna[i:i+3]
    if codon == "ATG":
        start_positions.append(i)

print("Start codons at positions:", start_positions)
stop_codons = ["TAA", "TAG", "TGA"]
stop_positions = []

for i in range(len(dna)-2):
    codon = dna[i:i+3]
    if codon in stop_codons:
        stop_positions.append(i)

print("Stop codons at positions:", stop_positions)
orfs = []

for start in start_positions:
    for stop in stop_positions:
        if stop > start and (stop - start) % 3 == 0:
            orf = dna[start:stop+3]
            orfs.append(orf)

print("ORFs Found:", len(orfs))
for o in orfs:
    print(o)

    codon_table = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"_", "TAG":"_",
    "TGC":"C", "TGT":"C", "TGA":"_", "TGG":"W"
     }
    def translate(sequence):
      protein = ""
      for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        amino_acid = codon_table.get(codon, "")
        if amino_acid == "_":
            break
        protein += amino_acid
      return protein
for orf in orfs:
    protein = translate(orf)
    print("Protein:", protein)


