"""
Utility module for dealing with readability metrics of English text.
"""
from __future__ import annotations
 
__author__ = 'Aditya Bhaskar, adbhaska@ucsc.edu'
 
import math
import re
import sys

syllables_dict = {}
with open('/srv/datasets/syllables.txt', 'r') as f:
  count = 1
  for line in f:
    for char in line:
      if char == ';':
          count += 1
      x = re.sub(';', '', line)
      syllables_dict[x] = count
  f.close()
 
class Readability(str):
  """
  Represents a string that can be assessed for readability metrics of English text.
  """
 
  # I encourage you to add other methods!

  def __init__(self, string):
    self.string = string

  def valid_string(self):
    text = []
    x = self.string
    txt = x.split()
    for words in txt:
      word = re.sub("^-|-$|^'|'$", "", words)
      text.append(word)
    y = " ".join(text)
    return y

  def char_count(self):
    val_str = valid_string(self.string)
    char = 0
    for i in range(len(val_str) - 1):
      if val_str[i].isalpha() or val_str.isdigit():
        char += 1
    return char

  def word_count(self):
    val_text = valid_string(self.string)
    x = re.split("[^A-Za-z0-9'-]", val_text)
    for words in x:
      if words == "":
        x.remove(word)
    return (len(x) - 1)

  def sentence_count(self):
    val_sentence = valid_string(self.string)
    x = re.split("[.?!]", val_sentence)
    return (len(x) - 1)

  def syllable_count(self):
    syll_val = valid_string(self.string)
    x = re.split("[^A-Za-z0-9'-]", syll_val)
    syll_count = 0
    for words in x:
      if words in syllables_dict:
        syll_count += 1
    return syllcount

  def polysyllable_count(self):
    polysyll_val = valid_string(self.string)
    x = re.split("[^A-Za-z0-9'-]", polysyll)
    polysyll_count = 0
    for words in x:
      if words in syllables_dict:
        if syllables_dict[words] > 2:
          pollysyll_count += 1
    return polysyllcount

  def words(self):
    val_words = valid_string(self.string)
    x = re.split("[^A-Za-z0-9'-]", val_words)
    for words in x:
      if words == "":
        x.remove(words)
    return x

  def polysyllable(self):
    polysyll_val = valid_string(self.string)
    x = re.split("[^A-Za-z0-9'-]", polysyll_val)
    for words in x:
      if words in syllables_dict:
        if syllables_dict[words] < 3:
          x.remove(words)
    return x

  def sentences(self):
    val_sent = valid_string(self.string)
    x = re.split("[!.?]", val_sent)
    y = []
    for ele in x:
      m = tuple(re.split(" ", ele))
      y.append(m)
    return y

  def automated_readability_index(self) -> float:
    """
    Calculates and returns the automated readability index of this text.
    See: https://en.wikipedia.org/wiki/Automated_readability_index
    """
    characters = char_count(self.string)
    words = word_count(self.string)
    sentences = sentence_count(self.string)
    ARI = (4.71 * (characters / words)) + (0.5 * (words / sentences)) - 21.43
    return ARI
 
  def coleman_liau_index(self) -> float:
    """
    Calculates and returns the Coleman–Liau index of this text.
    See: https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
    """
    Letters = char_count(self.string)
    Sentences = sentence_count(self.string)
    Words = word_count(self.string)
    L = (Letter / Words) * 100
    S = (Sentences / Words) * 100
    CLI = (0.0588 * L) - (0.296 * S) - 15.8
    return CLI
 
  def flesch_kincaid_grade(self) -> float:
    """
    Calculates and returns the Flesch–Kincaid grade level of this text.
    See: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level
    """
    total_words = word_count(self.string)
    total_sentences = sentence_count(self.string)
    total_syllables = syllable_count(self.string)
    fkg = 206.835 - (1.015 * (total_words / total_sentences)) - (84.6 * (total_syllables / total_words))
    return fkg
 
  def smog_grade(self) -> float | None:
    """
    Calculates and returns the SMOG grade of this text,
    or None if the text contains fewer than 30 sentences.
    See: https://en.wikipedia.org/wiki/SMOG
    """
    number_of_polysyllables = polysyllable_count(self.string)
    number_of_sentences = sentence_count(self.string)
    grade = (1.0430 * (math.sqrt(number_of_polysyllables * (30 / number_of_sentences)))) + 3.1291
    if number_of_sentences < 30:
      grade = None
    return grade
