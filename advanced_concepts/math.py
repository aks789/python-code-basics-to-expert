import math
import random
import pdb

#help(math)

value=5.5

print(math.floor(value))

print(math.ceil(value))

print(round(value))

print(math.log(10,10))

print(math.sin(10))

print(random.randint(1,10))

random.seed(101)

print(random.randint(0,100))

mylist = list(range(0,20))

print(mylist)

print(random.choice(mylist))

print(random.choices(population=mylist,k=30))

print(random.sample(population=mylist,k=10))

random.shuffle(mylist)

print(mylist)

print(random.uniform(a=0,b=100))

print(random.gauss(mu=0,sigma=3))

x = [1,2,3]
y =2
z=3

result = y+z
pdb.set_trace()
result2 = x+z
