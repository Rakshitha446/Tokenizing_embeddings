import nltk
nltk.download("punkt")
nltk.download("punkt_tab")

from nltk.tokenize import word_tokenize

text = "Hello! I am learning Natural Language Processing."

tokens = word_tokenize(text)

print(tokens)