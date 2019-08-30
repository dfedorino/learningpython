"""
items = dict()
items['phone'] = 1 # "phone" is a label to call out the value 1
items['money'] = 12
items['keys'] = 3
print(items)
"""
"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)
"""
# this is a pattern to create a little histogram out of the list and an empty dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
# ddd.get(key, default value) - if there is already a value in the dictionary
# .get() method helps to find the value under the key. If there is no such a
# key, .get() method DOESN'T change the dictionary, it just simply returns the
# default value to prevent a traceback
