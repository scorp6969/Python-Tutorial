# 2d lists = a list of lists

drinks = ['coffee', 'soda', 'tea']
dinner = ['pizza', 'burger', 'hotdog']
dessert = ['ice-cream', 'cake']

foods = [drinks, dinner, dessert]

for food in foods:
    print(food)

print(foods[0][1])
print(foods[1][1])
print(foods[2][1])

# extend method - merges different list into one
f = []
f.extend(drinks)
f.extend(dinner)
f.extend(dessert)

print(f)
