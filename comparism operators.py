temperature = int(input('temperature: '))
if temperature > 30:
    print("it's a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("it's a wonderful day, enjoy your day")

name = input('please enter your name: ')
if len(name) < 3:
     print('name too short')
elif len(name) >= 6:
    print('name too long')
else:
    print('name looks good')

