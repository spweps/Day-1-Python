num1 = 42 #data type, primative, number
num2 = 2.3 #data type, primative, number
boolean = True #data type, primative, boolean
string = 'Hello World' #data type, primative, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #data type, composite, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #data type, composite, list, boolean value
fruit = ('blueberry', 'strawberry', 'banana') #data type, composite, list
print(type(fruit)) #function, parameter, return
print(pizza_toppings[1]) #function, return, index return
pizza_toppings.append('Mushrooms') #data type, composite, list, add value
print(person['name']) #function, parameter, return
person['name'] = 'George' #data type, composite, list
person['eye_color'] = 'blue' #data type, composite, list
print(fruit[2]) #function, return, indexed return

if num1 > 45: #conditional, if
    print("It's greater") #function, return list
else: #conditional, else
    print("It's lower") #function, return list

if len(string) < 5: #conditional, if, data
    print("It's a short word!") #function, return, list
elif len(string) > 15: #conditional, else if, data
    print("It's a long word!") #function, return, list
else: #conditional, else,
    print("Just right!") #function, return, list

for x in range(5): #for loop, 
    print(x) #function, return
for x in range(2,5): #for loop, start stop
    print(x) #function, return
for x in range(2,10,3): #for loop, start stop increment
    print(x) #function, return
x = 0 #data type, primative, number
while(x < 5): #while loop, 
    print(x) #function, return
    x += 1 #while loop, increment

pizza_toppings.pop() #data type, composite, list, delete last value
pizza_toppings.pop(1) #data type, composite, list, delete item at index 1

print(person) #function, return
person.pop('eye_color') #data type,composite, list, delete
print(person) #function, return

for topping in pizza_toppings: #for loop, data type, composite, list
    if topping == 'Pepperoni': #conditional, if
        continue
    print('After 1st if statement') #function, return, list
    if topping == 'Olives': #conditional, if
        break

def print_hello_ten_times(): #function, parameter
    for num in range(10): #for loop, sequence
        print('Hello') #function, return, list

print_hello_ten_times() #function

def print_hello_x_times(x): #function, paramter, data type
    for num in range(x): #for loop, sequence
        print('Hello') #function, return, data type, list

print_hello_x_times(4) #function, return

def print_hello_x_or_ten_times(x = 10): #function, parameter
    for num in range(x): #for loops, sequence
        print('Hello') #function, return, data type, list

print_hello_x_or_ten_times() #function, return
print_hello_x_or_ten_times(4) #function, paramter, return


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)