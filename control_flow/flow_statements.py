hungry = True

if hungry:
    print("Feed Me !!!")
else:
    print("Dont feed me !!!!")


my_iterable = [1,2,3]

for item in my_iterable:
    if (item % 2) ==0:
        print(item)

my_string = 'akriti'

for char in my_string:
    print(char)

for gh in 'akshay':
    print('love you')

tup = (1,2,3)
for item in tup:
    print(item)

my_list = [(1,2),(3,4),(5,6),(7,8)]
for item in my_list:
    print(item)

for (a,b) in my_list:
    print(a)
    print(b)

my_dict = {'k1':1,'k2':2,'k3':3}

for item in my_dict:
    print(item)

for item in my_dict.items():
    print(item)

for item in my_dict.values():
    print(item)

i = 2

while i<3:
    print(f'current value of i is {i}')
    i=i+1
else:
    print('what')

x = [1,2,3]

for item in x:
    if item==2:
        break
    else:
        print(item)


for num in range(10):
    print(num)

my_list=list(range(10))

for item in my_list:
    print(item)

index_count=0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1

word = 'abcde'

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200]

for item in zip(mylist1,mylist2,mylist3):
    print(item)

y = 'x' in ['x',2,3]
print(y)

print(min(mylist1))
print(max(mylist3))

from random import shuffle

print(shuffle(mylist1))

print(mylist1)

from random import randint

print(randint(0,100))

result = input('Enter a number here: ')

print(type(result))

mylist = []

for item in 'hello':
    mylist.append(item)

print(mylist)

mylist = [letter for letter in 'hello']

print(mylist)

mylist = [num**2 for num in range(1,10)]

print(mylist)

mylist = [num for num in range(1,10) if num % 2 ==0]

print(mylist)

celcius = [0,10,20,34.5]

farenheit = [( (9/5)*temp +32 ) for temp in celcius]

print(farenheit)

mylist = []

for x in [2,4,6]:
    for y in [100,200]:
        mylist.append(x*y)

print(mylist)

mylist = [x*y for x in [2,4,6] for y in [100,200]]

print(mylist)

st = 'Print only the words that start with s in this sentence'

for item in st:
    print(item.split())
