from math import radians, sin, cos, tan

a = radians(float(input('Enter a angle: ')))

values = [sin(a), cos(a), tan(a)]

def round_two(v):
  return round(v, 2)

values = list(map(round_two, values))

print(f'''Sine: {values[0]}
Cosine: {values[1]}
Tangent: {values[2]}''')
