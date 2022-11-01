## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass 

## Dog is-a Animal
class Dog (Animal):

    def __init__(self, name):
        ## Dog has-a name attribute
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ## Cat has-a name attribute
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a attribute name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##Employee has-a attribute name
        super(Employee, self).__init__(name)
        ##Employee has-a attribute salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish:
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

##satan is-a Cat with attribute name "Satan"
satan = Cat("Satan")

## mary is-a Person with a name "Mary"
mary = Person("Mary")

## Mary has an attribute pet that is satan
mary.pet = satan

## frank is-a Employee with attributes name "Frank" and salary 120_000
frank = Employee("Frank", 120_000)

## frank has-a attribute pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
