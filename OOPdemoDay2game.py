from random import randint

class Trooper:
    game_name = "Star Wars Dojo Duel"
    everyone = []
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
        self.weapon = "Blaster"
        self.health = 100
        Trooper.everyone.append(self)
    
    def fight(self, foe):
        rand_attack = randint(0, self.attack)
        foe.health -= rand_attack
        if foe.health > 0:
            print(f"{self.name} damages {foe.name} with a {self.weapon} by {rand_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of {rand_attack} using their {self.weapon}")
        return self

    def heal(self):
        rand_health = randint(1, 100)
        future_health = self.health + rand_health
        if Trooper.can_heal(future_health):
            self.health += rand_health
            print (f"{self.name} healed by {rand_health} | Current Health: {self.health}")
        else:
            self.health = 100
            print(f"{self.name} health can't go above 100")
        return self
    
    @classmethod
    def all_fighters(cls):
        print("Fighters")
        for fighter in cls.everyone:
            print(fighter.name, fighter.weapon)
    
    @staticmethod
        def can_heal(future_health)
            if future_health > 100:
                return False
            else:
                return True

class Jedi():
    def __init__(self, name, attack):
        self.trooper = Trooper("Finn", 25)
        self.name = name

class Jedi(Trooper): #inheritance 
    def __init__(self, name, attack):
        super().__init__(name, attack):
        self.trooper = Trooper("Finn", 25)
        self.health = 200
        self.weapon = "Light Saber"
        self.force_push_attack = 50
    
    def force_push(self, foe):
        foe.health -= self.force_push_attack
        if(foe.health >0):
            print(f"{self.name} damages {foe.name} with a Force Push by {self.force_push_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with a Force Push")
        return self

    def heal(self):
        rand_health = randint(1, 200)
        future_health = self.health + rand_health
        if Jedi.can_heal(future_health):
            self.health += rand_health
            print (f"{self.name} healed by {rand_health} | Current Health: {self.health}")
        else:
            self.health = 200
            print(f"{self.name} health can't go above 200")
        return self
        
    @staticmethod
        def can_heal(future_health):
            if future_health > 200:
                return False
            else:
                return True

class Sith(Jedi):
    def __init__(self, name, attack):
        super().__init__(name, attack)
        #inherited everything from Jedi and then from Trooper
        self.force_lightning_attack = 70
    
    def force_lightning(self, foe):
        foe.health -= self.force_lightning_attack
        if(foe.health>0)
            print(f"{self.name} damages {foe.name} with a Force Lightning by {self.force_lightning_attack")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with a Force Lightning Attack")
        return self


vader = Sith("Darth Vader", 75)
print(vader.name) #inheritance stops elongated dot notation
print(vader.attack)
print(vader.health)
print(vader.weapon)
vader.heal()
vader.fight(vader)

obi = Jedi("Obi Wan", 75)
print(obi.trooper.name)
print(obi.trooper.health)

rex = Trooper("Rex", 15)
cody = Trooper("Cody", 12)

print(rex.health)  #dot notation
print(rex.attack)
print(cody.name)

rex.fight(cody)
cody.fight(rex)
cody.heal()

vader.force_lightning(obi)
vader.force_lightning(obi).fight(obi).heal().fight(obi) #make sure to return self in above methods when strining together otherwise it runs first method and stops

# print(f"Welcome to  {Trooper.game_name)")
# print(f"{rex.name} vs {cody.name}")
# print(f"{rex.name}: Attack - {rex.attack} | Health: {rex.health}")
# print(f"{cody.name}: Attack - {cody.attack} | Health: {cody.health}")

# rex = {
#     "name": "Rex"
#     "attack": 15,
#     "weapon": "Blaster Rifle"
#     "health": 100
# }

# fett = {
#     "name": "Fett"
#     "attack": 25,
#     "weapon": "Bolas"
#     "health": 100
# }

# print(rex["name"])
# print(rex["attack"])
# print(rex["weapon"])
# print(rex["health"])
# print(fett["name"])
# print(fett["attack"])
# print(fett["weapon"])
# print(fett["health"])
