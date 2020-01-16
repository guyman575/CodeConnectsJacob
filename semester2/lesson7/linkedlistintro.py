# https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png
from linkedlist import Node
from linkedlist import LinkedList
letterlist = LinkedList()
letterlist2 = LinkedList()
head = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
head.next = node2
node2.next = node3
node3.next = node4
node4.next = None
letterlist.head = head
# letterlist.printList()
# letterlist.pushFront("X")
# letterlist.printList()
# letterlist.pushBack("Z")
# letterlist.printList()
letterlist2.pushBack("Y")
letterlist2.printList()