"""Module Rosalind"""

amino = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N',
         'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
         'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S',
         'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
         'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
         'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
         'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
         'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
         'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
         'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
         'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
         'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
         'UAA': 'O', 'UAC': 'Y', 'UAG': 'O', 'UAU': 'Y',
         'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
         'UGA': 'O', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
         'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'}

"""amino = {}

with open(/srv/datasets/amino, 'r') as f:
    for line in f:
        splitLine = line.split()
        newDict[int(splitLine[0])] = ",".join(splitLine[1:])
"""


def valid_rna(rna: str):
    """
        Checks if the rna is valid or not
    """
    if rna is not None:
        rna_length = int(len(rna))
        codon = int(rna_length / 3)
        if rna_length % 3 == 0 and codon >= 12:
            val_str = True
        else:
            val_str = False
    else:
        val_str = False
    return val_str


def prot(rna: str):
    """
      Calculates and returns the protein string encoded by an RNA string, or None if the encoding
      is invalid. A valid encoding consists of 12 or more codons, where the first is start codon
      'AUG', followed by at least 10 more non-stop codons, and then a stop codon. (The shortest
      known protein is length 11: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3864261/)

      Amino-acid encoding information shall be taken from the dict represented by variable amino.

      :param rna: An RNA string (assumed to contain characters in 'ACGU', with len(rna) % 3 == 0).
      :return: The protein string encoded by rna, or None if the the encoding is invalid.
    """
    rna_length = int(len(rna))
    codon = int(rna_length / 3)
    no_of_codons = int(rna_length / codon)
    list_rna = []
    list_amino = []
    if rna is not None:
        for i in range(0, rna_length, no_of_codons):
            div = rna[i: i + no_of_codons]
            list_rna.append(div)
        UAA_count = list_rna.count('UAA')
        UAG_count = list_rna.count('UAG')
        UGA_count = list_rna.count('UGA')
        if list_rna[0] == 'AUG' and (list_rna[codon - 1] in ('UAA', 'UAG', 'UGA')):
            for RNA in list_rna:
                temp = amino[RNA]
                if temp == 'O':
                    break
                list_amino.append(temp)
            amino_acid = ""
            amino_acid = amino_acid.join(list_amino)
        else:
            amino_acid = None
    else:
        amino_acid = None
    stop_count = UAA_count + UAG_count + UGA_count
    if stop_count > 1:
        amino_acid = None
    if amino_acid is not None:
        if len(amino_acid) < 12:
            amino_acid = None
    else:
        amino_acid = None
    return amino_acid


def valid_amino(a_a: str):
    """
        Checks if the amino acid is valid or not
    """
    if a_a is not None:
        amino_len = int(len(a_a))
        if amino_len >= 12:
            val_amino = True
        else:
            val_amino = False
    else:
        val_amino = False
    return val_amino


def potential_proteins(rna: str):
    """Calculates and returns all potential valid protein encodings in an RNA string. Any protein
    valid according to function prot() shall be considered valid by this function as well.
    Amino-acid encoding information shall be taken from the dict represented by variable amino.
    :param rna: An RNA string (assumed to contain characters in 'ACGU').
    :return: A list of the possible proteins in the RNA, in the order encountered in the RNA."""
    rna_length = int(len(rna))
    codon = int(rna_length / 3)
    no_of_codons = int(rna_length / codon)
    list_rna = []
    list_amino = []
    pot_prot = []
    if rna is not None:
        for i in range(0, rna_length, no_of_codons):
            div = rna[i: i + no_of_codons]
            list_rna.append(div)
        UAA_count = list_rna.count('UAA')
        UAG_count = list_rna.count('UAG')
        UGA_count = list_rna.count('UGA')
        if list_rna[0] == 'AUG' and (list_rna[codon - 1] in ('UAA', 'UAG', 'UGA')):
            for RNA in list_rna:
                temp = amino[RNA]
                if temp == 'O':
                    break
                list_amino.append(temp)
            amino_acid = ""
            amino_acid = amino_acid.join(list_amino)
        else:
            amino_acid = None
    else:
        amino_acid = None
    stop_count = UAA_count + UAG_count + UGA_count
    if stop_count > 1:
        amino_acid = None
    if amino_acid is not None:
        if len(amino_acid) < 12:
            amino_acid = None
    else:
        amino_acid = None
    if amino_acid is not None:
        amino_len = len(amino_acid)
        if rna is not None:
            for i in range(0, amino_len - 1):
                if amino_acid[i] == 'M':
                    protein = amino_acid[i: amino_len]
                    if len(protein) >= 12:
                        pot_prot.append(protein)
        else:
            pot_prot = None
    else:
        pot_prot = None
    return pot_prot
