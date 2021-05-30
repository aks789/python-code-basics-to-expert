import re

text = "The agent's phone number is 408-555-1234. Call soon!"

print('phone' in text)

pattern = 'phone'

print(re.search(pattern,text))

match = re.search(pattern,text)

print(match.span())

text = 'My phone once, my phone twice'

match = re.search(pattern,text)

print(match)

matches = re.findall(pattern,text)
print(matches)
print(len(matches))

for match in re.finditer(pattern,text):
    print(match.span())
    print(match.group())