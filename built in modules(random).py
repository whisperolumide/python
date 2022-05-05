# picking three numbers randomly within a range of numbers
import random

for i in range(3):
    print(random.randint(0, 10))


# randomly picking an item from a list
import random

members = ['omoloja', 'olumide', 'ahmed', 'kunle']
leader = random.choice(members)
print(leader)

# dice game
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

