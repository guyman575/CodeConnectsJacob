# from collections import defaultdict

def letterCount(sentance):
    my_alphabet = {}
    lower_sentance = sentance.lower()
    for letter in lower_sentance:
        if letter.isalpha():
            my_alphabet[letter] = my_alphabet.get(letter, 0) + 1
            # if letter not in my_alphabet:
            #     my_alphabet[letter] = 1
            # else:
            #     my_alphabet[letter] += 1
    return my_alphabet



my_sentance = "Example sentance for letter count exercise"
my_counts = letterCount(my_sentance)
print(my_counts)
print(my_counts.values())
print(list(my_counts))

for key, value in my_counts.items():
    print(key, value)

for item in my_counts.items():
    print(item)

