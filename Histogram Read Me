# Histogram of 5-Letter Word Values

## Overview

This script visualizes the distribution of numerical values of randomly sampled 5-letter words using a histogram.

Each word's value is calculated as the sum of letter positions:

* `a = 1`, `b = 2`, ..., `z = 26`

---

## Features

* Generates 5-letter word combinations
* Samples first 1000 words
* Converts words into numeric values
* Displays distribution using a histogram

---

## Requirements

* Python 3.x
* NumPy
* Matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

---

## How It Works

### 1. Letter Mapping

```python
letter_to_num = {ch: idx+1 for idx, ch in enumerate(alphabet)}
```

### 2. Generate Words

```python
gen = (''.join(c) for c in itertools.product(alphabet, repeat=5))
```

### 3. Sample Words

```python
words_sample = [next(gen) for _ in range(1000)]
```

### 4. Convert to Numeric Values

```python
word_values = [sum(letter_to_num[ch] for ch in word) for word in words_sample]
```

### 5. Plot Histogram

```python
plt.hist(word_values, bins=26)
```

---

## Output

* A histogram showing frequency distribution of word values
* X-axis: Sum of letter values (range: 5 to 130)
* Y-axis: Frequency

---

## Important Insight

* Minimum value: `aaaaa` → **5**
* Maximum value: `zzzzz` → **130**
* Distribution tends toward a **normal-like shape** due to combinatorics

---

## Limitations

* Only uses first 1000 generated combinations (not random sampling)
* Not fully representative of all 11.8M possibilities

---

## Possible Improvements

* Use random sampling instead of sequential:

```python
import random
```

* Increase sample size for better distribution
* Save histogram as an image:

```python
plt.savefig("histogram.png")
```

---

## Use Cases

* Data visualization practice
* Statistical distribution analysis
* Feature engineering exploration

---

## Author Notes

This script demonstrates how combinatorial datasets can produce predictable statistical patterns when mapped numerically.

---
