# Five Letter Word Dataset Generator

## Overview

This project generates all possible 5-letter combinations using lowercase English alphabets (`a–z`) and stores them in a CSV file. Each word is assigned a numerical value based on the sum of its letters' positions in the alphabet.

Example:

* `abcde` → 1 + 2 + 3 + 4 + 5 = **15**

---

## Features

* Generates all possible 5-letter combinations (`26^5 = 11,881,376`)
* Maps letters to numerical values (`a=1`, `b=2`, ..., `z=26`)
* Outputs data into a structured CSV file
* Efficient generation using iterators (`itertools.product`)

---

## Requirements

* Python 3.x
* NumPy

Install dependencies:

```bash
pip install numpy
```

---

## How It Works

### 1. Alphabet Setup

```python
alphabet = string.ascii_lowercase
```

### 2. Letter-to-Number Mapping

```python
letter_to_num = {ch: idx + 1 for idx, ch in enumerate(alphabet)}
```

### 3. Generate Combinations

Uses Cartesian product:

```python
itertools.product(alphabet, repeat=5)
```

### 4. Compute Word Value

Each word is converted into a numeric value:

```python
value = sum(letter_to_num[ch] for ch in word)
```

### 5. Save to CSV

Output file:

```
five_letter_dataset.csv
```

Format:

```
Word,Value
abcde,15
aaaaa,5
zzzzz,130
```

---

## Notes on Performance

* Total rows generated: **~11.8 million**
* File size can exceed **hundreds of MB**
* Generation may take several minutes depending on system performance

---

## Optional Sampling (Already in Code)

This line:

```python
sample = np.fromiter(gen, dtype='<U5', count=1000)
```

creates a **sample of 1000 words**, but it is not used in CSV writing.

---

## Potential Improvements

* Add progress tracking (e.g., tqdm)
* Limit dataset size via parameter
* Parallelize generation for speed
* Store in binary formats (e.g., `.npy`, `.parquet`) for efficiency

---

## Use Cases

* Machine learning datasets
* Pattern analysis
* Cryptography experiments
* Statistical modeling

---

## Author Notes

This script prioritizes completeness over memory efficiency by writing directly to disk instead of storing everything in RAM.

---
