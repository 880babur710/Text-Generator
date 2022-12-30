from nltk.tokenize import regexp_tokenize
from collections import Counter
import random


token_lst = []
bigram_dict = {}
file = input()
with open(file, "r", encoding="utf-8") as text_file:
    for line in text_file:
        text = line.strip('\n')
        token_lst.extend(regexp_tokenize(text, r"[\S]+"))

# creating bigram dict
for i in range(len(token_lst)):
    if i != len(token_lst) - 1:
        bigram_dict.setdefault(token_lst[i], []).append(token_lst[i + 1])

# modifying `bigram_dict`: the values(tails) becomes a dictionary
for head in bigram_dict:
    tail_dict = Counter(bigram_dict[head])
    bigram_dict[head] = tail_dict

# creating word chain
for _ in range(10):
    # checking if the first word is capitalized
    first_word = random.choice(token_lst)
    while not first_word[0].isupper() or first_word[-1].endswith((".", "!", "?")):
        first_word = random.choice(token_lst)
    word_chain = [first_word]

    # finding the remainging tokens to make a complete sentence
    while len(word_chain) < 5 or not word_chain[-1].endswith((".", "!", "?")):
        head = word_chain[-1]
        tail_lst = list(bigram_dict[head].keys())
        weight_lst = list(bigram_dict[head].values())
        next_word = random.choices(tail_lst, weight_lst, k=1)
        word_chain.append(next_word[0])
    print(" ".join(word_chain))
