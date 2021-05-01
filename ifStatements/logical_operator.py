# logical operators - and, or, not are used to check if two or more conditional statement is true

temp = int(input('What is the temperature outside?: '))

if temp >= 0 and temp <= 30:
    print('The temperature is good today!\nGo Outside!!')
elif temp < 0 or temp > 30:
    print('The temperature is not good today!\nStay Inside!!')
