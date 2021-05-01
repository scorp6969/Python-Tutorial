# while loop = a statements that will execute its block of code as long as its condition is true

# method 1
# name = ""

# while len(name) == 0:
#     name = input('Enter your name: ')

# print('Hello ' + name)

# method 2
name = None

while not name:
    name = input('Enter your name: ')

print('Hello ' + name)