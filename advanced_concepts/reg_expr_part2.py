import re

text = "The agent's phone number is 408-555-1234. Call soon!"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)

print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern,text)

print(results.group(3))