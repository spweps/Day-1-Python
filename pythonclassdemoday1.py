my_money = 15
print (type(my_money))
    #type adds variable type to printout--classification

if my_money > 10:
    print ("I'm happy")
else:
    print ("I'm broke and sad")
    #pass -- allows code to continue on


likes_bbq = True
likes_fruit = False
weight = 190.5
iq = 142
name = "Scott"
age = "40"
print(len(age))
#strings have length, numbers do not unless formatted as a string
#str, int, float (adds decimal), complex (adds variables) are conversions
#type shows what kind of data type it is

if likes_bbq and weight > 150:
    weight += 10
    age = int(age) + 5
    print(name + " weighs " + str(weight) + " lbs " + age + " years old ")
elif likes_fruit or iq > 140:
    weight -=20
    print(weight)
else :
    print(weight)
