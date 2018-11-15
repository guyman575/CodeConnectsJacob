def runnerup(scores):
    current_highest = 0
    for elt in scores:
        if elt > current_highest and elt < max(scores):
            current_highest = elt
    return current_highest


scores = [2, 3, 6, 6, 5] # 5
print(runnerup(scores))
