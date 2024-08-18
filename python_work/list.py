bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[1])
print(bicycles[-1])

messaje = f"My first bicycle was {bicycles[1]}"
print(messaje)

bicycles[0] = "another"
print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'bmw')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop(2)
print(f"My last motorcycle I own was a {popped_motorcycles}")
print(motorcycles)

# Remove
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is to expensive for me")

# Exercise

people = ["santy", "valentina", "sebastian", "chris"]

print(f"would you like to assist to my party {people[0]}?")
print(f"would you like to assist to my party {people[1]}?")
print(f"would you like to assist to my party {people[2]}?")
print(f"would you like to assist to my party {people[3]}?")


cant_make_it = people.pop(1)
new_person = 'orlando'
print(f"hello everyone {cant_make_it} cannot make it, see you all later")
people.append(new_person)
print(people)

for person in people:
    print(f"hello everyone {person} cannot make it, see you all later")


new_guests = ["Caro", "Ana", "Flor Alba"]
print(f"Hello everyone we found a bigger table")

people.insert(0, new_guests[0])
people.insert(3, new_guests[1])
people.append(new_guests[2])

print(people)

for person in people:
    print(f"Hello {person} we would like to invite you to my party! Would you like to assist?")


print(f"That me again, unfortunately we can invite just two people")
person_remove = people.pop()
print(f"Sorry {person_remove} we cannot invite you to the dinner")
person_remove = people.pop()
print(f"Sorry {person_remove} we cannot invite you to the dinner")
person_remove = people.pop()
print(f"Sorry {person_remove} we cannot invite you to the dinner")
person_remove = people.pop()
print(f"Sorry {person_remove} we cannot invite you to the dinner")
person_remove = people.pop()
print(f"Sorry {person_remove} we cannot invite you to the dinner")

del people[0]
del people[0]

print(people)

# sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# sort list temporarily
cars_v2 = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars_v2, reverse=True))
print(cars_v2)

# reverse
cars_v3 = ['bmw', 'audi', 'toyota', 'subaru']
cars_v3.reverse()
print(f"reverse: {cars_v3}")

# length

print(len(cars_v3))


visit_places = ["calafate", "lisboa", "buenos aires", "madrid"]
print(visit_places)
print(sorted(visit_places))
print(sorted(visit_places, reverse=True))
visit_places.reverse()
print(visit_places)
visit_places.sort()
print(visit_places)
visit_places.sort(reverse=True)
print(visit_places)
visit_places.reverse()
print(visit_places)
visit_places.sort()
print(visit_places)

print(len(new_guests))

last_item = visit_places[-1]
print(last_item)


