# https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png
from linkedlist import Node
from linkedlist import LinkedList

letterlist = LinkedList()
letterlist.insert("A",0)
letterlist.pushFront("B")
letterlist.pushBack("Y")
letterlist.pushBack("Z")
letterlist.printList()
print(letterlist.find("Z").data)
letterlist.insert("J", 3)

letterlist.insert("X", 0)
letterlist.printList()
print(letterlist.size())