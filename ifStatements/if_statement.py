# if statement - a block of code that will execute if its condition is true

age = int(input('How old are you?: '))

if age == 100:
    print('You are century old.')
elif age >= 18:
    print('You are an adult.')
elif age < 0:
    print('You havn\'t been born yet.') # '\' is used as escape character
else:
    print('You are a child.')