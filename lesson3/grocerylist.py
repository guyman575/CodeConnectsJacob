def getGroceryList(restock, pantry):
    return []


RESTOCK_AMOUNTS = {"Eggs": 2, "Milk": 1, "Bread": 2,"Cereal": 1, "Apples": 10, "Bananas": 3}
PANTRY = {"Eggs": 1, "Milk": 0, "Bread": 0,"Cereal": 1, "Apples": 3, "Bananas": 5}
print(getGroceryList(RESTOCK_AMOUNTS, PANTRY))