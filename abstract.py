from abc import ABC,abstractmethod

class Abstract(ABC):

    @abstractmethod
    def sum(self):
        pass

class MyClass(Abstract):

    def sum(self):
        print("Overriding sum")
    
    def run(self):
        print("Hello from run")

# obj = Abstract()
obj = MyClass()

obj.sum()
obj.run()