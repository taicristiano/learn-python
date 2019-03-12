from Person import Person #import class

class Male(Person):
    sex = 'Male';
malePerson = Male('Tai Cristiano', 27, True)
print(malePerson.getName())
print(malePerson.getAge())
print(malePerson.getSex())