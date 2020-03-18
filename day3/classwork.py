class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("I am a dog. My name is", self.name)


class Labrador(Dog):
    def __init__(self, owner, name):
        super().__init__(name)
        self.owner = owner
    
    def bark(self):
        print("I am a Labrador. My master is", self.owner)
    
class GermanShepherd(Dog):
    def __init__(self, owner, name):
        super().__init__(name)
        self.owner = owner

dog = Dog("Nymeria")
labrador = Labrador("Bikalpa", "Ghost")
shepherd = GermanShepherd("Krishna", "Summer") 

shepherd.bark()