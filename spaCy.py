import spacy

# Create a blank English tokenizer
nlp = spacy.blank("en")

text = "Hello! I am learning Natural Language Processing."

doc = nlp(text)

print("spaCy Tokens:")

for token in doc:
    print(token.text)