# scope = The region that a variable is recognized. A cariable is only available from inside the region it is created. A global and locally scoped versions of a varaiable can be created
# python follows LEGB rule
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

name = 'rocky'  # global scope (available inside and outside of func)

def display_name():
    name = 'rambo'  # local scope (available inside of func)
    print(name)

display_name() 
print(name)
