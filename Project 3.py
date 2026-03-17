import string
import itertools
import numpy as np
import csv


alphabet = string.ascii_lowercase

letter_to_num = {ch: idx + 1 for idx, ch in enumerate(alphabet)}

gen = (''.join(c) for c in itertools.product(alphabet, repeat=5))

sample = np.fromiter(gen, dtype='<U5', count=1000)




with open("five_letter_dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Word", "Value"])

    for word in (''.join(c) for c in itertools.product(alphabet, repeat=5)):
        value = sum(letter_to_num[ch] for ch in word)
        writer.writerow([word, value])
