# *args = parameter that will pack all arguments into a tuple. useful so that a function can accept a varying amount of arguments

def add(*args): # can name args with anything bt * is compulsory
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7))