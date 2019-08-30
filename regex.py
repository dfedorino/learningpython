import re

hand = open('file.txt')
count = 0
lst = list()
for line in hand:
    numbers = re.findall('[0-9]+', line)
    if numbers == [] : continue
    lst.append(numbers)
for i in lst:
    print(i)
