
sentances = [
    'I really like _n.',
    'I ate a very _a _n today for lunch.',
    'I have a noun which is _n and also an adjective which is _a this is an example',
]

def mad_lib_for_sentance(sentance):
    new_sentance = ""
    start = 0
    for i in range(0,len(sentance)):
        if sentance[i] == "_":
            word = ""
            if sentance[i+1] == "a":
                word = input("Give me an adjective.")
            elif sentance[i+1] == "n":
                word = input("Give me a noun.")
            new_sentance += sentance[start:i] + word
            start = i+2
    new_sentance += sentance[start:]
    return new_sentance

# here
for i in range (0,len(sentances)):
    print(str(i + 1) + ". " + sentances[i])
sentance_number = input("Pick a sentance number.")
print(mad_lib_for_sentance(sentances[int(sentance_number) - 1]))
            


