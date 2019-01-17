from abc import ABC, abstractmethod

class AbstractList(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def append(self,item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def get(self,pos):
        pass


class MyList(AbstractList):

    def __init__(self):
        super().__init__()
        self.data = []

    def append(self,item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def get(self,pos):
        return self.data[pos]

class MyOtherList(AbstractList):

    def __init__(self):
        super().__init__()
        self.data = []

    def append(self,item):
        self.data.insert(0,item)

    def pop(self):
        val = self.data[0]
        del self.data[0]
        return val

    def get(self,pos):
        return self.data[pos]


def doThingsToAList(theList):
    if(isinstance(theList,AbstractList)):
        theList.append(7)
        theList.append(1)
        theList.append(1)
        theList.append(8)
        return theList.get(1) + theList.pop()

listA = MyList()
listB = MyOtherList()
doThingsToAList(listA)
doThingsToAList(listB)
print(listA.data)
print(listB.data)