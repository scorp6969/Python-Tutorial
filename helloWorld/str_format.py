# str.format() = optional method that gives users more control when displaying output

animal = 'cow'
item = 'moon'

# print('The {} jumped over the {}'.format('cow', 'moon'))

# positional argument
# print('The {1} jumped over the {0}'.format(animal, item))
# print('The {0} jumped over the {0}'.format(animal, item))

# keyword argument
# print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))  
# print('The {animal} jumped over the {animal}'.format(animal='cow', item='moon'))

text = 'The {} jumped over the {}'
print(text.format(animal, item))