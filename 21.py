name = input('Enter your full name: ')

print(f'Your name in uppercase is: {name.upper()}')
print(f'Your name in lowercase is: {name.lower()}')
print(f"Your name has {len(name) - name.count(' ')} letters")

first = name.split()[0]
print(f'Your first name is {first} and has {len(first)} letters')
