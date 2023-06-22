"""The program takes DNA strings as input and gets Amino Acid string as the output."""

import rosalind
import sys

# rna = input()
rna = sys.stdin.read()
if rosalind.valid_rna(rna):
    amino_acid = rosalind.prot(rna)
else:
    amino_acid = None
if rosalind.valid_amino(amino_acid):
    pot_prot = rosalind.potential_proteins(rna)
else:
    pot_prot = None
