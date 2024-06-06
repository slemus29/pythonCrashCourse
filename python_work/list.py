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