class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    def who_am_i(self):
        print("I am a Dog")

my_dog = Dog()

print(my_dog.who_am_i())


class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"Author is {self.author} and title is {self.title}"

    def __len__(self):
        return self.pages

mybook = Book('Wainan dua','Akshay',10)

print(mybook)
print(len(mybook))

del mybook

print(mybook)