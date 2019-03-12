class Person:
    name = ""
    age = 0
    male = False

    def __init__(self, name, age, male):
        print('INIT')
        self.name = name
        self.age = age
        self.male = male

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setMale(self, male):
        self.male = male

    def getMale(self):
        return self.male

    def getSex(self):
        print("Sex: %s" %(self.sex))

    # def __del__(self):
        # print('Delete class')
# person = Person('Tai Cristiano', 27, True)
# print(person.name)
# print(person.age)
# print(person.male)
# print(person.getName())
# person.setName('tainhot')
# print(person.getName())
