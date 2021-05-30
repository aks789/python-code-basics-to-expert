def func():
    return 1

func()

def hello():
    print('Hello!')

greet = hello

greet()

del hello

greet()

def hello1(name = 'Jose'):
    print('This is the hello1() function')

    def greet():
        return '\tThis is the greet() function inside of hello1'

    def welcome():
        return '\tThis is welcome() function inside of hello1'

    if name == 'Jose':
        return greet
    else:
        return welcome



my_new_func = hello1()

print(my_new_func())

def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()

print(some_func())

def hello():
    return 'Hi Akshay'

def other(some_func):
    print('Pther code runs here')
    print(some_func())

print(hello())

print(hello)

other(hello)

##_____________________________


def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function!')

        original_func()

        print('Some extra code, after the original function!')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')

#decorated_func = new_decorator(func_needs_decorator)

#decorated_func()

func_needs_decorator()