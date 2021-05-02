# set - collection of value which is unordered, unindexed. no duplicate value

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}

# add elements in set
utensils.add('napkin')

#remove element from set
utensils.remove('fork')

# clear the set
utensils.clear()

dishes.update(utensils)
# or
utensils.update(dishes)

# union
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

# comparision
print(dishes.difference(utensils))
print(utensils.difference(dishes))

print(dishes.intersection(utensils))

