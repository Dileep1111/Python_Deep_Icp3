import csv
from collections import Counter
count = 0
codon_dict = {}
with open('codon.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
            codon_dict[row[0]] = row[1]
    print(codon_dict)
while True:
  codon_seq = input(" enter the input sequence: ")
  if len(codon_seq)%3 != 0 :
    print("DNA sequence not valid. Give a valid one")
    continue

  codon_seq_list = [codon_seq[i:i+3] for i in range(0, len(codon_seq), 3)]
  print("the individual codon sequence is: ", codon_seq_list)
    codon_names = list(map(lambda x: codon_dict[x], codon_seq_list))
    break
name_counts = Counter(codon_names)
print("the names and count of codons: ", name_counts)

