number = 3.14159
num1 = 1000
num2 = 15

print('The value of pi is {}'.format(number))
print('The value of pi is {:.2f}'.format(number))
print('The value of pi is {:.3f}'.format(number))
print('')
print('The number is {:,}'.format(num1))    # gives comma at thousand place
print('The number is {:b}'.format(num2))    # binary representation
print('The number is {:o}'.format(num2))    # octal representation
print('The number is {:X}'.format(num2))    # hexadecimal representation(upper)
print('The number is {:x}'.format(num2))    # hexadecimal representation(lower)
print('The number is {:E}'.format(num2))    # scientific notation(upper)
print('The number is {:e}'.format(num2))    # scientific notation(lower)
