from nltk.tokenize import regexp_tokenize
from collections import Counter
import random


token_lst = []
bigram_dict = {}
trigram_dict = {}
word_chain = []
first_two_tokens = []
file = input()
with open(file, "r", encoding="utf-8") as text_file:
    for line in text_file:
        text = line.strip('\n')
        token_lst.extend(regexp_tokenize(text, r"[\S]+"))

# creating bigram dictionary
# for i in range(len(token_lst)):
#     if i != len(token_lst) - 1:
#         bigram_dict.setdefault(token_lst[i], []).append(token_lst[i + 1])

# creating trigram dictionary
for j in range(len(token_lst)):
    if j < len(token_lst) - 2:
        head = token_lst[j] + " " + token_lst[j + 1]
        trigram_dict.setdefault(head, []).append(token_lst[j + 2])

# modifying `bigram_dict`: the values(tails) becomes a dictionary
# for head in bigram_dict:
#     tail_dict = Counter(bigram_dict[head])
#     bigram_dict[head] = tail_dict

# modifying `trigram_dict`; the values(tails) becomes a dictionary
for head in trigram_dict:
    tail_dict_2 = Counter(trigram_dict[head])
    trigram_dict[head] = dict(tail_dict_2)

# creating word chain
for _ in range(10):
    # checking if the first word is capitalized
    trigram_head = [head for head in trigram_dict]   # "What do"
    first_two_tokens = random.choice(trigram_head).split()
    while not first_two_tokens[0][0].isupper() or \
            first_two_tokens[0].endswith((".", "!", "?")):
        first_two_tokens = random.choice(trigram_head).split()
    word_chain.extend(first_two_tokens)

    # finding the remainging tokens to make a complete sentence
    while len(word_chain) < 5 or not word_chain[-1].endswith((".", "!", "?")):
        head = word_chain[-2] + " " + word_chain[-1]
        tail_lst = list(trigram_dict[head].keys())
        weight_lst = list(trigram_dict[head].values())
        next_chain_word = random.choices(tail_lst, weight_lst, k=1)
        word_chain.append(next_chain_word[0])
    print(" ".join(word_chain))
    word_chain = []


if __name__ == '__main__':
    pass
