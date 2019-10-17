import math

a = float(input('Value of first side: '))
b = float(input('Value of second side: '))

c = math.sqrt((a ** 2) + (b ** 2))

print(f'Hypotenuse: {round(c, 2)}')
