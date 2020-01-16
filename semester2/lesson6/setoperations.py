set_A = {1,4,5,9,10,77,3,21,2}
set_B = {1,12,5,47,3,99,100,101}
set_C = {1000, 1001, 1002}
set_D = {1,4,5}

A_union_B = set_A.union(set_B)
# A_union_B = set_A | set_B
A_intersect_B = set_A.intersection(set_B)
# A_union_B = set_A & set_B
A_minus_B = set_A.difference(set_B)
# A_minus_B = set_A - set_B
A_symdiff_B = set_A.symmetric_difference(set_B)
# A_symdiff_B = set_A ^ set_B
print(A_union_B)
print(A_intersect_B)
print(A_minus_B)
print(A_symdiff_B)

print(set_D.issubset(set_A))

print(set_D <= set_A)
# This one is for proper subset
print(set_D < set_A)
print(set_D <= set_D)
print(set_D < set_D)

