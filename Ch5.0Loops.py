# Chapter 5 - Loops and Iteration
# Loops (Repeated Steps) have iteration variables that change each time through a loop...
# Often these iteration variables go through a sequence of numbers.

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(0)

# INFINITE LOOPS
# while loops are called 'infinite loops' because they keep going until a logical condition becomes 'False'.
# Loops we have seen so far are pretty easy to examine to see if they will terminate or if they will be 'infinite loops'.
# Sometimes it is a little harder to be sure if a loop will terminate.


# n =5
# while n>0:
#     print('Lather')
#     print('Rinse')
# print('Dry off!')

# "Zero-Trip" Loop

n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!')

# BREAKING OUT OF LOOP
# The break statement ends the current loop and jumps to the statement immediately following the loop.
# It is like a loop test that can happen anywhere in the body of the loop.

while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

# CONTINUE - another loop control statement to finishing an iteration.
# It works differently then 'Break'

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# DEFINITE LOOPS (FOR LOOPS)
# quite often we have a 'list' of items of the 'lines in a file' - effectively a 'finite set' of things
# we can write a loop to run the loop once for each of the items in a set using the Python 'for' construct.
# these loops are called 'definite loops' because they execute an exact number of times.
# we say the "definite loops iterate through the members of a set".

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done!')

# How FOR LOOPS works
# (1) iteration variable 'iterates' through the 'sequence' (ordered set)
# (2) 'block (body)' of code executed once for each value in the 'sequence'
# (3) 'iteration variable' moves through all of the values 'in' the 'sequence'





