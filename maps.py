def square(num):
    return num**2

nums=[1,2,3,4]
for item in map(square,nums):
    print(item)

print(list(map(square,nums)))

print(list(map(lambda num : num **2,nums)))

print(list(filter(lambda num : num % 2==0,nums)))

x = 50

def func():
    global x
    print(f'Value if X is {x}')
    x = 200


func()
print(x)

import string

print(string.ascii_lowercase)


