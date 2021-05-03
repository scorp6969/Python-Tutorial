# give padding to the value

name = 'rocky'

# positional argument + padding
print('Hello my name is {0:10}. Nice to meet you.'.format(name))

# left align
print('Hello my name is {:<10}. Nice to meet you.'.format(name))

# right align
print('Hello my name is {:>10}. Nice to meet you.'.format(name))

# center align
print('Hello my name is {:^10}. Nice to meet you.'.format(name))
