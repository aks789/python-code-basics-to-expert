d = {'k1':1,'k2':2}
d1 = {x:x**2 for x in range(10)}

print(d1)

## zip creates an iterator which will aggregate two or more iterables
d2 = {k:v**2 for k,v in zip(['a','b'],range(2))}

print(d2)

for k in d1.values():
    print(k)

## ADVANCED LISTS ##
l = [1,2,3,4]

l.append(5)

print(l)

print(l.count(10))

print(l.extend([6]))

print(l)
## Extend adds each element of iterable and append adds exact iterable

## Element from index param has to be in list else it throws error
print(l.index(2))

print(l.insert(2,8))

print(l)

ele = l.pop()

print(ele)

ele1 = l.pop(0)

print(ele1)

# Removes the first occurrence of the element in the list
l.remove(2)

print(l)

l.reverse()

print(l)

l.sort()
print(l)