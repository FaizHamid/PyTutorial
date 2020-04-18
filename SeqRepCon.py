# Sequential Repeated Conditional
# Python short story about how to count words in a file

from itertools import count
from pip._vendor.distlib.compat import raw_input

# A word used to read data from a user
name = input('Enter file: ')
handle = open(name, 'r')

# A sentence about updating one of the many counts
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# A paragraph about how to find the largest item in the list
bigcount = None
bigword = None
# for word, count is counts.items():
if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count

print(bigword, bigcount)
