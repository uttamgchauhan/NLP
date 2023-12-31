# -*- coding: utf-8 -*-
"""Zipf's Law.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GL6Bg6OU_h5rWuy1J9VdZIxPuhP2LIf7
"""

import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

corpus = ['Natural Language Processing with NLTK',
             'Natural Language gets developed over the time',
             'Language Processing is very important',
             'Natural Language Processing is an important scientific field',
             'Natural Language Analysis',
             'Natural Language Processing',
             'Natural Language Understanding',
             'Natural Language Understanding']

# The corpus under study is large generally. Hence, we use
# Download the "punkt" resource
nltk.download('punkt')

flat_corpus=[]
for sent in corpus:
    flat_corpus.extend(nltk.word_tokenize(sent))
print(flat_corpus)

# Compute the frequency distribution of words in the corpus
fdist = FreqDist(flat_corpus)

# Compute the ranks and frequencies of the words
ranks = list(range(1, len(sorted_words) + 1))
frequencies = [fdist[word] for word in sorted_words]

# Print words, frequencies, and ranks in a formatted table
print("{:<12s}{:<12s}{:<6s}".format("Word", "Frequency", "Rank"))
print("---------------------------------")
for rank, word in enumerate(sorted_words, 1):
    frequency = fdist[word]
    print("{:<16s}{:<12d}{:<6d}".format(word, frequency, rank))

# Plot the ranks vs. frequencies on a log-log scale
plt.loglog(ranks, frequencies, marker='.')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title("Zipf's Law Test")
plt.grid(True)
plt.show()

from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Specify the file path within Google Drive
file_path = '/content/drive/MyDrive/FundamentalsNLP/lmcorpus.txt'

# Read the file
with open(file_path, 'r') as file:
    corpus = file.read()

# Load the Reuters corpus
nltk.download('reuters')
corpus = nltk.corpus.reuters.sents()

# Read the file from the Colab runtime
file_path = '/content/lmcorpus.txt'  # Replace with the actual file path

with open(file_path, 'r') as file:
    corpus = file.read()