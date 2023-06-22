"""Contains class Protein for working with protein-related information."""

# Code Source: Jeffrey Bergamini, Professor, CSE30, Spring 2021
# URL: https://jeff.cis.cabrillo.edu/classes/cse30s21/lecture_materials/week_04

__author__ = 'Aditya Bhaskar, adbhaska@ucsc.edu'


class Protein:
  """ Represents an immutable sequence of amino acids. """

  def __init__(self, aminos=None):
    """Constructs a protein from a sequence of amino acids.
    See: http://rosalind.info/problems/prot/
    :param aminos: A sequence of single-character strings, expected to be in the amino-acid alphabet
    :raise: ValueError if aminos contains characters not found in the amino-acid alphabet"""
    self.aminos = list(aminos) if aminos else []
    if any(base not in 'QWERTYIPASDFGHKLCVNM' for base in self.aminos):
      raise ValueError('Illegal characters in Amino sequence')

  def __add__(self, addition):
    """The + operator concatenates two proteins.
    :param addition: a sequence of single-character strings in the amino-acid alphabet
    :return: a new Protein object representing the concatenation of this protein and the addition
    :raise: ValueError if addition contains characters not found in the amino acid-alphabet"""
    return Protein(self.aminos + list(addition))

  def __eq__(self, other):
    """Two proteins will be equal if they represent the same sequence of amino acids.
    :param other: a sequence of single-character strings in the amino-acid alphabet
    :return: whether this protein is equal to the other"""
    if isinstance(other, Protein):
      return self.aminos == other.aminos
    else:
      return self.aminos == list(other)

  def __getitem__(self, key):
    """The [] operator allows users to retrieve individual amino acids in a protein by index,
    or a Protein object representing a slice of this protein.
    :param key: an index or slice
    :return: a single-character string (if key was an index) or a Protein (if key was a slice)
    :raise: IndexError if index is out of range"""
    if isinstance(key, slice):
      return Protein(self.aminos[key])
    else:
      return self.aminos[key]

  def __len__(self):
    """ Returns the length of this protein, i.e. its number of amino acids. """
    return len(self.aminos)

  def __repr__(self):
    """ Returns a string that would result in reproducing this protein when interpreted. """
    return f"Protein('{self}')"

  def __str__(self):
    """ Returns a string containing the amino-acid letters for this protein. """
    return ''.join(self.aminos)

  def mass(self):
    """Returns the mass of this protein (in Daltons), according to the monoisotopic mass table.
    See: http://rosalind.info/problems/prtm/
    mass_table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
                  'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
                  'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
                  'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
                  'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}"""

    mass = 0
    mass_table = {}
    if len(mass_table) == 0:
      with open('/srv/datasets/amino-monoisotopic-mass', 'r') as f:
        for line in f:
          (key, val) = line.split()
          mass_table[key] = val
        f.close()
    for char in self.aminos:
      amino_mass = float(mass_table.get(char))
      mass += amino_mass
    return mass
