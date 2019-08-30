# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") # "mbox-short.txt"
fh = open(fname)
count = 0
lst = []
for i in fh:
    if not i.startswith("X-DSPAM-Confidence"):
        continue
    count += 1
    findex = i.find("0")
    fdnumber = float(i[findex:])
    lst.append(fdnumber)
    a = 0
    for i in lst:
        a += i
print("Average spam confidence:", a / count)
