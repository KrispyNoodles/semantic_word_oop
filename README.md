# 🧠 semantic_word_oop

A fun side project that explores **word semantics** through **object-oriented programming** and **pretrained word embeddings**.

This Python class lets you perform vector arithmetic on words—such as:

```python
king - man + woman = queen
```

## 🔍 What It Does

- Loads a pretrained word embedding model (e.g., GloVe, Word2Vec).
- Creates an instance of each word with attributes such as the original text and its corresponding vector.
- Supports intuitive vector arithmetic using operator overloading:
  - + for vector addition  
  - - for vector subtraction
- Prevents repeated use of words in analogy chains by applying stem-based exclusion, managed through a class-level variable `EXCLUDED_STEMS`.

---

## 🖼️ Example Visualization

Here's a vector space representation of some example results:

<img width="961" height="814" alt="semantic vector arithmetic" src="https://github.com/user-attachments/assets/a569c3bc-82d1-4bf2-ab75-9acffe826249" />

---

## 🚀 Quick Start

```python
from word_vector import WordVector

king = WordVector("king")
man = WordVector("man")
woman = WordVector("woman")

result = king - man + woman
result

# to ensure that the result isnt removed (making it repeatable)
WordVector.EXCLUDED_STEMS = []
```
