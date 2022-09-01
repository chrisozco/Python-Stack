import ninja

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
# noise() - prints out the pet's sound
    def noise(self):
        print(self.pet_noise)

Daisy = Pet('Daisy', 'Doge', 'Fetch', 'Barks')

