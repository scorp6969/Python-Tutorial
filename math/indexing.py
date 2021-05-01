# slicing = create substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = 'Rocky Rambo'

first_name = name[0:5]
last_name = name[6:11]

print('method 1')
print(first_name)
print(last_name)

f_name = name[:5]
l_name = name[6:]

print('')
print('method 2')
print(f_name)
print(l_name)

funky_name = name[::2]

print('')
print(funky_name)

reversed_name = name[::-1]

print('')
print(reversed_name)

