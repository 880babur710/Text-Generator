from nltk.tokenize import regexp_tokenize


token_lst = []
bigram_lst = []
file = input()
with open(file, "r", encoding="utf-8") as text_file:
    for line in text_file:
        text = line.strip('\n')
        token_lst.extend(regexp_tokenize(text, r"[\S]+"))

# creating bigram list and printing its size
for i in range(len(token_lst)):
    if i != len(token_lst) - 1:
        bigram = [token_lst[i], token_lst[i + 1]]
        bigram_lst.append(bigram)
print(f"Number of bigrams: {len(bigram_lst)}")


# print the elements of the bigram list
index_input = input()
while index_input != "exit":
    try:
        index = int(index_input)
        bigram = bigram_lst[index]
        print(f"Head: {bigram[0]} Tail: {bigram[1]}")
    except IndexError:
        print("Index Error. Please input an integer that is in the "
              "range of the corpus.")
    except ValueError:
        print("Type Error. Please input an integer.")
    index_input = input()
