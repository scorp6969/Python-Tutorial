# tuple = collection which is ordered and unchangable used to group together related data

student = ('rocky', 21, 'male')

print(student.count('rocky'))
print(student.index('male'))

for x in student:
    print(x)

if "rocky" in student:
    print('rocky is here!')