s = set()

s.add(1)
s.add(2)

print(s)

s.clear()

print(s)

s = {1,2,3}

sc = s.copy()

print(sc)

s.add(4)

print(s)
print(sc)

print(s.difference(sc))
print(s)
print(sc)
s.difference_update(sc)
print(s)
sc.discard(3)
print(sc)
s = {4,5}
sc = {4}
print(s.intersection(sc))
s.intersection_update(sc)
print(s)

print(s.isdisjoint(sc))
print(s.issubset(sc))
print(s.issuperset(sc))
print(s.symmetric_difference(sc))
print(s.union(sc))
s.update(sc)
print(s)