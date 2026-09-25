# BPE (Byte Pair Encoding)

from collections import Counter

def get_pairs(word):
    pairs = Counter()

    for i in range(len(word) - 1):
        pairs[(word[i], word[i + 1])] += 1

    return pairs


def merge_pair(pair, word):
    new_word = []
    i = 0

    while i < len(word):
        if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
            new_word.append(word[i] + word[i + 1])
            i += 2
        else:
            new_word.append(word[i])
            i += 1

    return new_word


def bpe(text, num_merges=5):
    words = text.lower().split()

    # Represent every word as characters
    word_tokens = [list(word) for word in words]

    for _ in range(num_merges):
        pair_counts = Counter()

        for word in word_tokens:
            pair_counts.update(get_pairs(word))

        if not pair_counts:
            break

        best_pair = pair_counts.most_common(1)[0][0]

        word_tokens = [
            merge_pair(best_pair, word)
            for word in word_tokens
        ]

    return word_tokens


text = "low lower lowest"

tokens = bpe(text, 5)

print("BPE Tokens:")
for token in tokens:
    print(token)