fhand = open("mbox-short.txt")
lst = list()
lst1 = list()
ddd = dict()
for line in fhand: # main purpose of the loop - to get a list with hours
    line = line.rstrip() # getting rid of whitespaces in the end of the string
    if not line.startswith('From ') : continue # getting rid of lines without "From "
    words = line.split() # making a list with words from a string
    lst.append(words[5]) # put an item to an existing list
for time in lst:
    hours = time.split(":")[0]
    lst1.append(hours)
for hour in lst1:
    ddd[hour] = ddd.get(hour, 0) + 1
sorted_list = sorted(list(ddd.items()))
for tuple in sorted_list:
    hour, count = tuple
    print(hour, count)
