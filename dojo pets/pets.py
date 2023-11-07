class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 1000
        self.noise = noise
        self.energy = 500

    def sleep(self, energy):
        self.energy += 25
        return self

    def eat(self, energy, health):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self, health):
        self.health += 5
        self.energy -= 15
        return self
    
    def noise(self):
        print(self.noise)
        return self
