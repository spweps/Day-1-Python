def add(a,b):
    x = a+b
    return x         #NECESSARY!  Returns are mandatory in orde to obtain value
add_val = add(2,5)
print(add_val)

def add(a=1, b=2):
    x = a+b
    return x
add_val = add(2)   #value replaces index A
print(add_val)




heroes = ("Iron Man", "Hulk", "Wonder Woman", "Thor")
villains = ["Thanos", "Joker", "Ultron", ["Marvel", "DC"]]

def say_hi(heroes):       #refer to previous heroes list created
    for i in heroes:
        if(type(i) ==str)
            print(f"Hi {i}")
say_hi(heroes)
say_hi(villains)