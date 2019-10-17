d = float(input('Distance (in meters): '))

print(f'''{d * 0.001}km
{d * 0.01}hm
{round(d * 0.1, 5)}dam
{d * 10}dm
{d * 100}cm
{d * 1000}mm''')
