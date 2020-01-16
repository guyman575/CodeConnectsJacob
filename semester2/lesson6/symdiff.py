# Everything which is in A, or B, but NOT both
def sym_diff(set_A, set_B):
    final_set = set()
    for value in set_A:
        if value not in set_B:
            final_set.add(value)
    for value in set_B:
        if value not in set_A:
            final_set.add(value)
    return final_set

set_1 = {5, 27, 34, 77, 92, 6, 14}
set_2 = {5, 26, 35, 77, 93, 6, 13}

if sym_diff(set_1, set_2) == set_1.symmetric_difference(set_2):
    print(True)

assert sym_diff(set_1, set_2) == set_1.symmetric_difference(set_2)