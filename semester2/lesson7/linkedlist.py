class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
        # here temp is None
    
    def pushFront(self, newData):
        newNode = Node(newData)
        temp = self.head
        self.head = newNode
        newNode.next = temp

    def pushBack(self, newData):
        newNode = Node(newData)
        temp = self.head
        if temp == None:
            self.head = newNode
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = newNode