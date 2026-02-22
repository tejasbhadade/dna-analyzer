dna = input("Enter DNA sequence: ").upper()
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
