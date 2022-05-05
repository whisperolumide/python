names = ["ahmed", 'kunle', 'taiye', 'tayo', 'kofo']
print(names[2:])
print(names[:])
names[1] = 'wale'
print(names)

# write a code to find the largest number in a list
numbers = [6, 7, 4, 2, 8, 7, 45]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

# list methods
numbers = [6, 7, 4, 2, 8, 7, 45]
numbers.append(10)
print(numbers)
numbers.insert(0, 5)
print(numbers)
print(69 in numbers)
numbers.sort()
print(numbers)

# write a python code to remove the duplicates in a list
numbers = [6, 7, 4, 2, 2, 7, 45]
new_number = []
for number in numbers:
    if number not in new_number:
        new_number.append(number)
print(new_number)


