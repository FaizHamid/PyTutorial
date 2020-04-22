# Chapter 6 - STRING
# String is a sequence of characters
# String literal uses quotes 'Hello' or "Hello"
# For strings, + means "concatenate"
# when a string contains numbers, it is still a 'String'
# We can convert numbers in a 'String' into a number using int().

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

str3 = '123'
# str3 = str3 + 1

x = int(str3) + 1
print(x)

# Reading and Converting
# we prefer to read data in using 'Strings' and then parse and convert the data as we need
# This gives us more control over error situations and/or bad user inputs
# raw input numbers must be 'converted' from Strings.

name = input('Enter your name: ')
print(name)

apple = input('Enter: ')
# x = apple - 10
x = int(apple) - 10
print(x)

# LOOKING INSIDE 'STRINGS'
# we can get any single character in a String using an index specified in 'Square Bracket'
# The index value must be an integer and starts at 'ZERO'
# The index value can be an expression this is computed

fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

# LEN FUNCTION
# Strings have Length - the built-in function 'len' gives us the length of a 'string'
# a 'Function' is some 'Stored Code' that we use. A function takes some 'input' and produces an 'output'

fruit = 'banana'
print(len(fruit))

# Looping through 'Strings'
# using a 'while variable' + an 'iteration variable' + a 'len function' = 'constructs a loop'
# to look at each of the letters in a 'String' individually

# using WHILE loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(fruit, letter)
    index = index + 1

# using FOR Loop
# a definite loop using a FOR statement is much more elegant
# the 'Iteration Variable' is completely taken care of by the FOR Loop

fruit = 'banana'
for letter in fruit:
    print(letter)

# Looping and Counting
# This is a simple loop that loops through each letter in a sting and counts the number of times the loop encounters
# the 'a' character

word = 'banana'
count = 0
for letter in word:  # 'letter' is the iteration variable
    if letter == 'a':
        count = count + 1
print(count)

# Looking deep into 'IN'
# the iteration variable 'iterates' through the 'sequence' (ordered set)
# the block (body) of the code is executed once for each value in the sequence
# the iteration variable moves through all of the values in the sequence

# STRING SLICING
# we can also look at any continuous section of a string using a 'colon operator'
# the second number is one beyond the end of the slice - "up to but not including"
# if the second number is beyond the end of the string, it stops at the end

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# if we leave of the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively
print(s[:2])
print(s[8:])
print(s[:])

# STRING CONCATENATION
# when the + operator is applied to strings, it means "concatenation"
a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

# Using 'IN' as 'Logical Operator'
# the 'IN' keyword can also be used to check to see if one string is 'IN' another string
# the 'IN' expression is a logical expression that returns 'True' or 'False' and can be used in an 'IF' statement
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print('Found it!')

# STRING COMPARISON
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word', + word + ', comes before banana.')
elif word > 'banana':
    print('Your word', + word + ', comes before banana.')
else:
    print('All right, bananas.')

# STRING LIBRARY
# Python has a number of string 'functions' which are in the 'String Library'
# these 'functions' are already 'built into' every string - we invoke them by appending the function to the string variable
# these 'functions' do not modify the original string, instead they return a new string that has been altered

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi there'.lower())

# Search and replace
# the 'replace()' function is like a 'search and replace' operation in a word processor
# it replaces all occurrences or the 'search string' with 'replacement string'
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
