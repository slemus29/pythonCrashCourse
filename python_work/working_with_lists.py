magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyon. That was a great magic show!")

# Exercise 1

pizzas = ['hawaiana', 'pepperoni', 'salami']

for pizza in pizzas:
    print(f"I like {pizza} pizza")
print('I really love pizza!')

animals = ['dolphin', 'shark', 'whale']

for animal in animals:
    print(f'The {animal} is a sea animal')
print('Those animals does not have grills')

# Numbers

for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

list_range = list(range(6))
print(list_range)

list_range_2 = list(range(2, 11, 2))
print(list_range_2)

#squares
squares = []
for value in range(11):
    square = value ** 2
    squares.append(square)
print(squares)


digits = list(range(1,11))
digits.pop()
digits.append(0)
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

# list comprenhensions

squares = [value**2 for value in range(0,11)]
print(squares)

# exercise

for value in range(1, 21):
    print(value)

# for value in range(1, 1000001):
#     print(value)

# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

for value in range(1, 20, 2):
    print(value)

for value in range(1, 10):
    print(value**3)

cubes = [value**3 for value in range(1,10)]
print(cubes)


#slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
print(players[1:3])

#copy list

food = ['pasta', 'rice', 'avocado']
friends_food = food[:]
print(food)
print(friends_food)

print(f"the first three items in the list are: {players[:3]}")
print(f"Three items from the middle are: {players[1:4]}")
print(f"The last Three items are: {players[-3:]}")

friends_pizzas = pizzas[:]
pizzas.append('cheese')
friends_pizzas.append('bufala')

print(f'My favorite pizzas are')
for pizza in pizzas:
    print(pizza)

print(f'My Friends favorite pizzas are')
for pizza in friends_pizzas:
    print(pizza)

# Tuples

dimensions = (200, 50)
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

restaurant_food = ('rice', 'beens', 'sushi', 'pizza', 'hamburger')
for food in restaurant_food:
    print(food)

# restaurant_food[2] = 'pasta'

restaurant_food = ('tacos', 'enchiladas', 'chilaquiles')
for food in restaurant_food:
    print(food)
