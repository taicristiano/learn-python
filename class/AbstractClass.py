from abc import ABC, abstractmethod

class AbstractClass(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    @abstractmethod # define abstract method
    def getFull(self):
        pass
class Person(AbstractClass):
    name = 'Tai nhot'
    age = 22
    def getFull(self):
        self.getName();
        self.getAge();

Person().getFull();