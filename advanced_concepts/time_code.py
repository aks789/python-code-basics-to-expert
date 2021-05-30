import time
import timeit

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))

start_time = time.time()

res = func_one(10000)

end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)

start_time = time.time()

res = func_two(10000)

end_time = time.time()

elapsed_time = end_time - start_time

print('\n')
print(elapsed_time)

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print("\n")
print(timeit.timeit(stmt,setup,number = 1000000))

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

print("\n")
print(timeit.timeit(stmt2,setup2,number = 1000000))