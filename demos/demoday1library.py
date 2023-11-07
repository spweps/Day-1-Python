Ironman = {
    "name": "Tony Stark",
    "bday": "5/29/1970",
    "weight": 160
    "powers":{
        "power1": "Genius"
        "power2": "Master Engineer"
        "power3": "wealthy AF"
    }
}#key value pairs



print(Ironman)
print(Ironman["name"])
Ironman["age"] = 51
print(Ironman)
value = Ironman.pop("bday") #pop removes from dictionary but can be stored as a value for later
print(Ironman)
del Ironman("weight")
villains[3].pop(1) #deletes indexed position

print(Ironman["powers"]["power1"])