import pets

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__ (self, data):
        self.first = data['first']
        self.last = data['last']
        self.treats = data['treats']
        self.pet_food = data['pet_food']
        self.pet = data['pet']

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walks(self):
        self.pet = self.pets.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet = self.pets.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def noise(self):
        self.pet = self.pets.noise()
        return self

chris = {'first': 'Chris', 'last': 'Orozco', 'treats': 'bone', 'pet_food': 'kibble', 'pet': 'Daisy'}
owner_chris = Ninja(chris)
