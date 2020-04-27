# Chapter 8 - LISTS
# Programming are of two types-
# (1) Algorithms - a set of rules or steps used to solve a problem
# (2) Data Structures - a particular way of organizing data in a computer

# What is not a collection
# most of our 'variables' have one value in them - when we put a new value in the variable, the old value is overwritten
x = 2
x = 4
print(x)

# A LIST is a kind of Collection
# collection allows us to put many values in a single "variable"
# collection is nice because we can carry all 'many values' around in one convenient package
friends = ['Joseph', 'Glen', 'Sally']
carryon = ['socks', 'shirts', 'perfume']

# LIST CONSTANTS
# a List constants are surrounded by square brackets [] and the elements in the list are separated by commas
# a List element can be any Python object - even 'another list'
# a List can be 'empty'

print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5, 6], 7])
print([])

# We already used lists
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

# LISTS and definite LOOPS - best pals
friends = ['Joseph', 'Glen', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done')


z = ['Joseph', 'Glen', 'Sally']
for x in z:
    print('Happy New Year: ', x)
print('Done')

# Looking inside Lists
# just like strings, we can get any single element in a list using an index specified in 'square brackets' []
friends = ['Joseph', 'Glen', 'Sally']
print(friends[1])

# LISTS are mutable
# Strings are 'immutable' - we can not change the content of the string - we must make a new string to make any change
fruit = 'Banana'
# fruit[0] = 'b'

x = fruit.lower()
print(x)

# Lists are 'mutable' - we can change an element of a list using the index operator
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

# How long is the List?
# the len() function takes a list as a parameter and returns the number of elements in the list
# actually len() tells us the number of elements of any set or sequence (such as strings)
greet = 'Hello World!'
print(len(greet))

x = [1, 2, 'joe', 99]
print(len(x))

# Using the 'Range Function'
#