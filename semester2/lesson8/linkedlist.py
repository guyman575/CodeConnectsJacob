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
    
    # Finds and returns the first node with a given value
    # None if no such node exists
    def find(self, value):
        temp = self.head
        while temp.data != value:
             temp = temp.next
        return temp

    # inserts a new node with value newData at position
    def insert(self, newData, position):
        newNode = Node(newData)
        before = self.head
        if position == 0:
            self.head = newNode
            newNode.next = before
            return
        after = self.head.next
        if after == None and position == 1:
            before.next = newNode
        else:
            for i in range (0,position-1):
                before = after
                after = after.next
            before.next = newNode
            newNode.next = after

    # deletes the node at the given position
    def deleteAt(self, position):
        pass

    # returns the size
    def size(self):
        temp = self.head
        i = 0
        while temp != None:
            temp = temp.next
            i = i + 1
        return i

    # -------------- STATIC METHODS BELOW HERE --------------
    # inserts a new node with value newData after otherNode
    @staticmethod
    def insertAfter(newData, afterNode):
        pass

    # deletes the node after otherNode
    @staticmethod
    def deleteNode(victim):
        pass


            