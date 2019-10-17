res = input('Enter something: ')

print(f'''Type: {type(res)}
Only spaces: {res.strip() == ''}
Is an number: {res.isdigit()}
Is alphabetic: {res.isalpha()} 
Is alphanumeric: {res.isalnum()}
Is uppercase: {res.isupper()}
Is downcase: {res.islower()}
Is capitalized: {res.istitle()}''')
