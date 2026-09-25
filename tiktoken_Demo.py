import tiktoken

# Load GPT-4/GPT-3.5 style tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

text = "Hello! I am learning Natural Language Processing."

tokens = encoding.encode(text)

print("Token IDs:")
print(tokens)

print("\nTokens:")

for token in tokens:
    print(encoding.decode([token]))