from nltk.tokenize import regexp_tokenize


token_list = []
file = input()
with open(file, "r", encoding="utf-8") as text_file:
    for line in text_file:
        text = line.strip('\n')
        token_list.extend(regexp_tokenize(text, r"[\S]+"))

print("Corpus statistics", f"All tokens: {len(token_list)}",
      f"Unique tokens: {len(set(token_list))}", sep="\n")

index_input = input()
while index_input != "exit":
    try:
        index = int(index_input)
        token = token_list[index]
    except IndexError:
        print("Index Error. Please input an integer that is in the "
              "range of the corpus.")
    except ValueError:
        print("Type Error. Please input an integer.")
    else:
        print(token)
    index_input = input()
