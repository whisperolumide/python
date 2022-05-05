# how to handle errors
try:
    age = int(input('age: '))
    risk = 2000
    income = risk / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print("Invalid value")

# "TRY" and "EXCEPT" block are used to handle errors in python
