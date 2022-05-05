class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 40
print(point1.x, point1.y)
point1.draw()
point1.move()

# Constructor
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi i'm {self.name}")


john = Person('john smith')
print(john.name)
john.talk()

bob = Person('bob smith')
bob.talk()


#
class Mammals:
    def walk(self):
        print("walk")


class Dog(Mammals):
    def bark(self):
        print("bark")


class Cat(Mammals):
    pass


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.walk()
