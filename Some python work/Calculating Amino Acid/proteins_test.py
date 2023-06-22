"""
Prints all potential proteins, one per line, encoded by DNA on standard input.
"""
import re
import sys
import rosalind

if __name__ == '__main__':
  # Use a regular expression to discard all non-A/C/GT characters, then transcribe the DNA to RNA
  rna = re.sub('[^ACGT]', '', sys.stdin.read()).translate({ord('T'): ord('U')})
  # Print the elements of the list returned by rosalind.potential_proteins(), one per line
  print('\n'.join(rosalind.potential_proteins(rna)))
