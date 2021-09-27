for i in range(10, -1, -1):  #range is exclusive of numbers
    print(i)

for i in "Why hello there":
    print(i)

heroes = ("Iron Man", "Hulk", "Wonder Woman", "Thor") #tuple here due to parenthesis
villains = ["Thanos", "Joker", "Ultron",["Marvel", "DC"]] #list due to brackets

for i in range(0, len(heroes)):
    print(i, heroes[i])

for i in heroes:
    print(i)

for i in villains:
    print(i)

for i in villains[3]:
    print(i)

librarys

Ironman = {
    "name": "Tony Stark",
    "bday": "5/29/70",
    "weight": 160,
    "powers":{
        "power1": "Genius"
        "power2": "Master Engineer"
    }
}

for i in Ironman:
    print(i, Ironman[i])

for i in Ironman["powers"]:
    print(i, Ironman["powers"][1])


while loops:

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Happy New Year")