# a = "Hello, world!"
# b = a.replace(",", " ")
# c = b.replace("!", " ")
# d = c.split()
# print (d[0], d[1])

signs = [",", "!"]
for i in signs:
    a = "Hello, world!"
    b = a.strip(i)
print(b)
