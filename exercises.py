# Print first 10 natural numbers using

i = 1
while i <= 10:
    print(i)
    i += 1

# program to print a pattern
'''
1
12
123
1234
12345
'''
i = 5
for i in range(1, i+1, 1):
    for j in range(1, i+1):
        print(j, end="")
    print("")

# Calculate the sum for all numbers from 1 to a given number
s = 0
n = int(input("Enter number: "))
for i in range(1, n+1, 1):
    s += i
print('Sum is:', s)

#OR
s = 0
n = int(input('Enter number: '))
i = sum(range(1, n+1))
print('sum is:', i)


# Write a program to display numbers that are (i) divisible by 5 (ii) if the number is > 150, skip (iii) if number is > 500, stop the loop

numbers = [12, 75, 25, 150, 180, 50, 5, 145, 525]
for number in numbers:
    if number > 500:
        break
    elif number > 150:
        continue
    elif number % 5 == 0:
        print(number)


# write a program to count the number of digits in a number

number = 234567812296
count = 0
while number != 0:
    number = number // 10
    count = count + 1
print("total number of digits is:", count)


"""
write a program to print the pattern:
54321
4321
321
21
1
"""

i = 5
k = 5
for i in range(0, i+1):
    for j in range(k-i, 0, -1):
        print(j, end="")
    print('')

#print a list in reversed order
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)

#OR
list = [20, 40, 60, 80, 100]
size = len(list) - 1
for i in range(size, -1, -1):
    print(list[i])

# display numbers from -19 to -1
for number in range(-19, 0, 1):
    print(number)

# use else block to display a message "done" after successful execution of for loop

i=5
for i in range(5):
    print(i)
else:
    print("'done'")

# write a program to display all prime numbers within a range

start = 9
stop = 50
print('Prime numbers between', start, 'and', stop, 'are: ')
for number in range(start, stop + 1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number)

# write a program to calculate the factorial of a given number

number = int(input("Enter number: "))
factorial = 1
if number < 0:
    print("factorial does not exist for negative numbers")
elif number == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print('The factorial of', number, "is", factorial)
