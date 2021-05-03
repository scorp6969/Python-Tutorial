# keyword arguments = arguments by an identifier when we pass them to a function The order of the arguments doesnt matter, unlike positional arguments Python knows the names of the arguments that our function recieves

def hello(first, middle, last):
    print('Hello ' + first + ' ' + middle + ' ' + last)


hello(last='rocky', middle='dude', first='rambo')