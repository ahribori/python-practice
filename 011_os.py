import os

print(os.getcwd())

print(os.listdir())

print(os.listdir('./module'))

files = os.listdir()
print(len(files))
print(type(files))

for file in files:
    if file.endswith('.py'):
        print(file)

