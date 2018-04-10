animals = ['dog', 'cat', 'cow']

print(animals)
print(type(animals))
print(animals[0])

print(animals[1:2])

animals.append('pig')
print(animals)

animals.insert(1, 'bird')
print(animals)

print(len(animals))

del animals[0]
print(animals)