# two string which contain the exact same
# characters with the same frequency
# "care" and "race" but NOT "racer" and "race"

# write a function which takes in two strings
# and returns the number of deletions required
# to make the strings anagrams
# stringA: runner
# stringB: near
# delete from A: r, n, u
# delete from B: a
# Answer: 4

# HINT: string.count("a") gives the number of "a" in string

def num_needed(stringA, stringB):
    total = 0
    for i in "abcdefghijklmnopqrstuvwxyz":
        total += abs(stringA.count(i) - stringB.count(i))

    return total

print(num_needed("runner","near"))