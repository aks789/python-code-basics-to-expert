import re

result = re.search(r'cat|dog','the dog is here')

print(result)

result = re.findall(r'. at','The cat in the hat sat there. ')
print(result)

phrase = 'there is 3 in 34 this letter'

pattern = '[^\d]+'
res = re.findall(pattern,phrase)

print(res)

phrase = 'This is a string! It has punc . How to remove it?'

pattern = r'[^!.? ]+'

res1 = re.findall(pattern,phrase)
print(' '.join(res1))
