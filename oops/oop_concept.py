class Dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.my_attr=breed
        self.name=name

    def bark(self,number):
        print('Woof!! My name is {} and number is {}'.format(self.name,number))


my_dog=Dog('Lab','akshay')

print(type(my_dog))

print(my_dog.my_attr)
print(my_dog.name)
print(my_dog.species)
my_dog.bark(12)

class Circle:

    pi = 3.14

    def __init__(self,radius=1):
        self.radius=radius
    def circumference(self):
        return Circle.pi * self.radius * 2

my_circle = Circle()

print(my_circle.circumference())