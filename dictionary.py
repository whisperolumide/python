user = {
    "name" : "omoloja ahmed",
    'age' : 28,
    'email' : 'omoloja@gmail.com',
    'school' : 'federal university of technology akure'
}
print(user["name"])
print(user.get('email'))
print(user.get('game', 'football'))
print(user.get('line'))

# write a code to translate digits to words
phone = input('phone: ')
digits = {
    '1' : 'one',
    '2' : 'two',
    '3': 'three',
    '4' : 'four'
}
output = ''
for ch in phone:
    output += digits.get(ch, '!') + ' '
print(output)

