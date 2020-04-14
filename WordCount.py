from itertools import count

from pip._vendor.distlib.compat import raw_input

name = raw_input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
# for word, count is counts.items():
if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count

print(bigword, bigcount)
