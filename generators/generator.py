def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

def create_cubes_gen(n):
    for x in range(n):
        yield x**3

for x in create_cubes_gen(10):
    print(x)

print(create_cubes_gen(10))

def fibonnaci_seq(n):

    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b

for x in fibonnaci_seq(10):
    print(x)

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))

s = 'hello'

for letter in s:
    print(letter)

s_iter = iter(s)

print(next(s_iter))




my_list = [1,2,3,4]
## ( paranthesis makes it a generator and same thing would be list if we used [ paranthesis
gen_comp = (item for item in my_list if item > 3)

for x in gen_comp:
    print(x)