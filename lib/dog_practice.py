class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self
    
    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog("Fido")
snoopy = Dog("Snoopy")

fido.breed = "Dalmation"
snoopy.breed  = "Beagle"

fido.breed
snoopy.breed

fido.showing_self()

fido = Dog("Fido")
fido.get_adopted("Sophie")
fido.owner