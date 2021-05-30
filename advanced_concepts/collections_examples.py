from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1,2,1,1,1,2,2,3,4,4]

print(Counter(mylist))

sentence = 'how many times does each word show up in this sentence  with a word'

print(Counter(sentence.split()))

letters = 'aaabbbbccccccccdddddddddddddddddd'

c = Counter(letters)

print(c.most_common())

print(list(c))

d = {'a':10}

print(d)

print(d['a'])

d = defaultdict(lambda: 0)

d['correct'] = 100
print(d['correct'])

print(d['wrong'])

print(d)

mytuple = (10,20,30)

print(mytuple[0])

Dog = namedtuple('Dog',['age','breed','name'])

nunny = Dog(age=10,breed='Pomerian',name='love')

print(type(nunny))

print(nunny)

print(nunny.name)