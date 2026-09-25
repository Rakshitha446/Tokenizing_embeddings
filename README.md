# Tokenization & Embeddings using Python

A beginner-friendly Natural Language Processing (NLP) project that demonstrates how different tokenization techniques convert text into tokens. The project includes implementations of Byte Pair Encoding (BPE), NLTK, spaCy, and OpenAI's tiktoken.

## Features

* Byte Pair Encoding (BPE) implementation
* Word tokenization using NLTK
* Tokenization with spaCy
* GPT-style tokenization using tiktoken
* Simple and beginner-friendly Python programs

## Technologies Used

* **Language:** Python 3
* **Libraries:** NLTK, spaCy, tiktoken

## Project Structure

```text
Tokenization_Embeddings/
├── BPE.py
├── nltk_tokenizer.py
├── spaCy.py
├── tiktoken_Demo.py
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install nltk spacy tiktoken
```

Download the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

Run any program individually:

```bash
python BPE.py
python nltk_tokenizer.py
python spaCy.py
python tiktoken_Demo.py
```

## Sample Output

```text
BPE Tokens:
['low']
['lower']
['lowes', 't']
```

## Applications

* Natural Language Processing (NLP)
* Large Language Models (LLMs)
* Chatbots
* Text Classification
* Text Preprocessing
