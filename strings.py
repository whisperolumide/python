course = 'Python for beginners'

course1 = "python's for beginners"

course2 = '''Hi josh
here is our first email to you.
takecare of yourself and good luck'''
print(course)
print(course1)
print(course2)
print(course[0:3])
print(course[0:])
print(course[:-1])

# formatted strings
first = 'john'
last = 'smith'
msg = first + ' [' + last + '] is a coder'
message = f'{first} [{last}] is a coder'
print(message)
print(msg)

# strings methods
course = 'my name is Omoloja'
print(len(course))
print(course.upper())
print(course.find('n'))
print(course.replace('Omoloja', 'Ahmed'))
print('Omoloja' in course)
print('omoloja' in course)
