import string
import itertools
import numpy as np
import matplotlib.pyplot as plt

# alphabet mapping
alphabet = string.ascii_lowercase
letter_to_num = {ch: idx+1 for idx, ch in enumerate(alphabet)}  # a=1, b=2, ..., z=26

# generator of 5-letter words
gen = (''.join(c) for c in itertools.product(alphabet, repeat=5))

words_sample = [next(gen) for _ in range(1000)]

# convert words to sum of letter positions
word_values = [sum(letter_to_num[ch] for ch in word) for word in words_sample]

# create histogram
plt.hist(word_values, bins=26, color='skyblue', edgecolor='black')
plt.title("Histogram of 5-letter word sums")
plt.xlabel("Sum of letters (a=1,..,z=26)")
plt.ylabel("Frequency")
plt.show()