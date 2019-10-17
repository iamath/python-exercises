import random

s = []

for i in range(4):
  s.append(input(f'Student {i + 1}: '))

print(f'Chosen student: {random.choice(s)}')
