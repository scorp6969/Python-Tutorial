# dictionary - a changable, unordered collection of unique kyy:value pairs. fast because they use hashing, allow us to access a value quickly

capitals = {
    'USA':'Washington DC',
    'India':'New Delhi',
    'Russia':'Moscow',
    'China':'Beijing',
    'Nepal':'Kathmandu'
}

capitals.update({'Germany':'Berlin'})

print(capitals['Russia'])

print(capitals.get('Germany'))

# for getting only keys
print(capitals.keys())

# for getting only values
print(capitals.values())

# for getting all items in dictionary
print(capitals.items())

capitals.pop('India')

for key, value in capitals.items():
    print(key, value)
