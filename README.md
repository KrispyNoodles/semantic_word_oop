# semantic_word_oop
A fun project that explores word semantics using object-oriented programming

This project provides a lightweight Python class for performing algebraic operations on word vectors—such as king - man + woman = queen—using pretrained embeddings like GloVe or Word2Vec.

Features include:

Easy-to-use WordVector class with + and - operator overloading

Stem-aware exclusion to prevent returning original or semantically similar input terms

Swappable pretrained models from gensim.downloader

Suitable for building semantic analogy tools, NLP experimentation, or educational demos.
