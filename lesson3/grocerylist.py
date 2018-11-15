def getGroceryList(restock, pantry):
    grocerylist = []
    if RESTOCK_AMOUNTS["Eggs"] > PANTRY["Eggs"]:
        grocerylist.append(str(RESTOCK_AMOUNTS["Eggs"] - PANTRY["Eggs"]) + " Eggs")
    if RESTOCK_AMOUNTS["Milk"] > PANTRY["Milk"]:
        grocerylist.append(f'{RESTOCK_AMOUNTS["Milk"] - PANTRY["Milk"]} Milk')
    if RESTOCK_AMOUNTS["Bread"] >PANTRY["Bread"]:
        grocerylist.append(f'{RESTOCK_AMOUNTS["Bread"] - PANTRY["Bread"]} Bread')
    if RESTOCK_AMOUNTS["Cereal"] > PANTRY["Cereal"]:
        grocerylist.append(f'{RESTOCK_AMOUNTS["Cereal"] - PANTRY["Cereal"]} Cereal')
    if RESTOCK_AMOUNTS["Apples"] > PANTRY["Apples"]:
        grocerylist.append(f'{RESTOCK_AMOUNTS["Apples"] - PANTRY["Apples"]} Apples')
    if RESTOCK_AMOUNTS["Bananas"] > PANTRY["Bananas"]:
        grocerylist.append(f'{RESTOCK_AMOUNTS["Bananas"] - PANTRY["Bananas"]} Bananas')
    
    
           
    return grocerylist


RESTOCK_AMOUNTS = {"Eggs": 2, "Milk": 1, "Bread": 2,"Cereal": 1, "Apples": 10, "Bananas": 3}
PANTRY = {"Eggs": 1, "Milk": 0, "Bread": 0,"Cereal": 1, "Apples": 3, "Bananas": 5}
print(getGroceryList(RESTOCK_AMOUNTS, PANTRY))

PANTRY['Eggs']
my_list = []
my_list.append("1 Egg")

something = RESTOCK_AMOUNTS["Eggs"] - PANTRY["Eggs"]