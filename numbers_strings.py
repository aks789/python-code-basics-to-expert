my_dog = 2
my_dog = "sammy"


print(my_dog);

# Exponent : **
# Square root : ** 0.5
# Square : my_dog ** 2


print(type(my_dog));

b = "I don't \n like you"

print(len(b));

print(b);

print(b[-1]);

print(b[2:7:2]);

print(b[::-1]);

name = "Sam"

## Below will give error as strings are immutable
# name[0]='P'

last_letters = name[1:];

new_name = 'P' + last_letters;

print(new_name);

# Multiplication of letters of string

new_name = last_letters * 10 ;

print(new_name);

x = 'hello world';

## Does not change actual value of x until you assign it back
print(x.upper()) ;

print(x);

print(x.split());

m_name = 'Akriti';

print('hello ' + m_name);

print('This is a {b} String {a} '.format(a = 'INSERTED' ,b= 'INSERTED AGAIN'));

result = 100/377;

## value:width.precisionf
print('The result is {r:1.3f}'.format(r = result))

print(f'The result is {result}');

def myfunc(name):
    print(f'Hello {name}')

myfunc('Akriti')
