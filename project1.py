# weight converter from either kilogram to gram or gram to kilogram

Weight = int(input('what is your weight: '))
unit = input('K(kg) or G(gram): ')
if unit.upper() == 'G':
    new_weight = Weight / 1000
    print(f'you are {new_weight} kilos')
else:
    new_weight = Weight * 1000
    print(f'you are {new_weight} gram')


