class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, pet_noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.pet_noise = pet_noise
        self.energy = 50
        self.health = 50

# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy = self.energy + 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health = self.health + 5
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print(self.pet_noise)

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__ (self, first, last, treats, pet_food, pet):
        self.first = first
        self.last = last
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bath(self):
        self.pet.noise()
        return self

Daisy = Pet('Daisy', 'Doge', 'Fetch', 'Barks')
owner_chris = Ninja('Chris', 'Orozco', 'bone', 'kibble', Daisy)


owner_chris.walk()
owner_chris.feed()
owner_chris.bath()