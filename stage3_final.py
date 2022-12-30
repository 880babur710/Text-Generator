from nltk.tokenize import regexp_tokenize
from collections import Counter


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

# print the elements of the bigram list
key_input = input()
while key_input != "exit":
    print(f"Head: {key_input}")
    try:
        tail_dict = bigram_dict[key_input]
        for tail, count in tail_dict.items():
            print(f"Tail: {tail}    Count: {count}")
    except KeyError:
        print("Key Error. The requested word is not in the model. "
              "Please input another word.")
    key_input = input()
