# 🧠 semantic_word_oop

A fun and educational project that explores **word semantics** through **object-oriented programming** and **pretrained word embeddings**.

This Python class lets you perform vector arithmetic on words—such as:

```python
king - man + woman = queen
```

📦 Built with Gensim's pretrained models, the project demonstrates how analogies and relationships between words can be represented mathematically using vector operations.

---

## 🔍 What It Does

- Loads a pretrained word embedding model (e.g., GloVe, Word2Vec).
- Wraps each word in an object for intuitive manipulation using Python operators:
  - `+` for vector addition
  - `-` for vector subtraction
- Prevents reuse of words by using stem-based exclusion.
- Supports custom embedding models with a simple method call.

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
print(result)  # Should return something close to "queen"
```
