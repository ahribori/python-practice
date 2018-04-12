person = {
    'name': '정현승',
    'age': 30,
}


person['gender'] = 'male'


print(person)

print(type(person))

print(len(person))

print(person['name'])

print(person.keys())

print(person.values())

print('name' in person.keys()) # true

print('phone' in person.keys()) # false

print(person['phone']) # error
