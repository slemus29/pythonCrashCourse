cars = ["bmw", "mercedes", "audi", "subaru", "toyota"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('hold the anchovies!')

age = 18
age_1 = 21
if age == 18:
    print("thats correct!")

print(age > 18)

print(age > 10 and age < 19)
print(age_1 > 18 or age > 18)

print('Checking Whether a Value Is in a List')

requested_topping_list = ['mushrooms', 'olives', 'onions']
print('mushrooms' in requested_topping_list)
print('pepperoni' in requested_topping_list)


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()} you can post a response!")    

# Exercise 1

car = 'mercho'
print("Is car == 'subaru' ? I predict is false")
print(car == 'subaru')

name = 'santy'
print("Is your name == 'Santy' ? I predict is true")
print(name.lower() == 'santy')

price = 5000
price_2 = 800

print("did the check overpass the money that we have which is 1000, I predict is true")
print(price > 1000)

print("Any of the checks is less than the money we have which is 1000, I predict is True")
print(price < 1000 or price_2 < 1000)

names = ['valentina', 'santy', 'chris']
user = 'sebastian'

if user not in names:
    print('You are Sebastian')

if user not in names:
    print('You are not Sebastian')


# else statatement

age = 18

if age >= 18:
    print("you are old enough to vote!")
else:
    print("Sorry, you're too young to vote")

age2 = 70
price =0

if age2 < 4:
    print("is free")
elif age2  < 18:
    price = 25
    print("you have to pay $25")
elif age2 < 65:
    price = 40
    print("you have to pay $40")
else:
    price = 20
    print("you have to pay $20")

print(f"the price of the ticket is {price}")

#indepen-dent if statements.

requested_toppings = ["pepperoni", "chicken"]

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")

#try your self

alien_color = "green"
if alien_color == 'green':
    print("player earn 5 points")
elif alien_color == 'yellow':
    print("player earn 10 points")
else:
    print("player earn 15 points")


age = 30

if age < 2:
    print("you are a baby!")
elif age < 4:
    print("you are a toddler!")
elif age < 13:
    print("you are a kid!")
elif age < 20:
    print("you are a teenager!")
elif age < 65:
    print("you are a adult!")
else:
    print("you are a elder")

favorite_fruts = ["banana", "apple", "strawberry"]


if 'apple' in favorite_fruts:
    print("You really like bananas!")
if 'grapes' in favorite_fruts:
    print("You really like bananas!")
if 'banana' in favorite_fruts:
    print("You really like bananas!")
if 'kiwi' in favorite_fruts:
    print("You really like bananas!")
if 'blueberries' in favorite_fruts:
    print("You really like bananas!")


requested_topping_list = []

if requested_topping_list:
    for topping in requested_topping_list:
        if topping == "olives":
            print(f"We're sorry, we are out of {topping}")
        else:
            print(f"adding {topping}")
else:
    print("Are you sure you want a plain pizza??")


print("---------")
available_toppings = ["pepperoni", "olives"]

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"adding {topping}")
    else:
        print(f"Sorry, we don't have {topping}.")
print("finished making your pizza")


#try your self

user_names = ["cgonzalez", "vlemus", "cgomez", "nsule", "trincon", "admin"]
# user_names = []

if user_names:
    for user in user_names:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ["sLemus", "cgonzalez", "admin"]
current_users_lower_case = []

for user in current_users:
    current_users_lower_case.append(user.lower())

for user in user_names:
    if user in current_users_lower_case:
        print(f"the user name {user} has already been used, you need to enter a new user name")
    else:
        print(f"the user name {user} is available")
