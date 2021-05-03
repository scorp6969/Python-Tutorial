# **kwargs = parameter that will pack all arguments into a ditionary, useful so that a function can accept a variying amount of keyword arguments

def hello(**kwargs):
    # print('Hello ' + kwargs['first'] + ' ' + kwargs['last'])
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')

hello(title='Mr.', first='rocky', middle='rambo', last='rambo')