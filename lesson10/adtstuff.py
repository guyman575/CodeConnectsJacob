from abc import ABC, abstractmethod


class MyInterface(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def method1(self,value1):
        pass

    @abstractmethod
    def method2(self):
        pass


class MyClass(MyInterface):

    def method1(self,value):
        print(value)

    def method2(self):
        print("Hello World")
        

myobj = MyClass(7)
myobj.method1(5)


