def getGroceryList(restock, pantry):
    grocerylist = []
    for key, needed in RESTOCK_AMOUNTS.items():
        current = PANTRY[key]
        if current >= needed:
            continue
        grocerylist.append(key + " " + str(needed - current))

    
    
           
    return grocerylist


RESTOCK_AMOUNTS = {"Eggs": 2, "Milk": 1, "Bread": 2,"Cereal": 1, "Apples": 10, "Bananas": 3}
PANTRY = {"Eggs": 1, "Milk": 0, "Bread": 0,"Cereal": 1, "Apples": 3, "Bananas": 5}
what_is_needed = getGroceryList(RESTOCK_AMOUNTS, PANTRY)
for item in what_is_needed:
    print(item)


# print(list(PANTRY.items()))
# a, b, c = (1,2,3)
# print(a,b,c)

# for key, value in PANTRY.items():
#     print(key, value)