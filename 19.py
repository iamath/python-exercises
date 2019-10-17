import random

s = []

for i in range(4):
  s.append(input(f'Student {i + 1}: '))

random.shuffle(s)

print(f'Order of presentation: {s}')
