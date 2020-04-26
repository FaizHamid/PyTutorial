# Chapter 7 - Reading Files

# OPENING A FILE
# before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file
# this is done with the 'open()' function
# open() returns a "file handle" - a variable used to perform operations on the file
# Similar to "file -> Open" in a Word Processor

# USING OPEN
# handle = open(filename, mode)
# fhand = open('mbox.txt', 'r')
# returns a handle use to manipulate the file
# filename is a string
# mode is option and should be 'r' if we are planning to read the file and 'w' if we want to write the file

fhand = open('file/self-driving-car')
print(fhand)

# New line Characters
# we use a special character called "newline" to indicate when a line ends
# we represent it as '\n' in strings
# 'Newline' is still a open character not two

stuff = 'Hello\nWorld!'
print(stuff)

stuff = '\nHello\nWorld!'
print(stuff)

stuff = 'X\nY\n'
print(stuff)

len(stuff)

# READING - file Handle as a Sequence
# a file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
# we can use the for statement to iterate through a sequence
# Remember - a sequence is an ordered set

xfile = open('file/self-driving-car')
for line in xfile:
    print(line)

# COUNTING LINES in a file
# open a file read-only
# use a 'for' loop to read each line
# count the lines and print out the number of lines

fhand = open('file/self-driving-car')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Reading the 'WHOLE' file
# we can read the whole file (newlines and all) into a 'Single String'

fhand = open('file/self-driving-car')
inp = fhand.read()
print(len(inp))
print(inp[:18])

# SEARCHING THOROUGH A FILE
# we can put an if statement in our for loop to ony print lines that meet some criteria

fhand = open('file/self-driving-car')
for line in fhand:
    if line.startswith('Our'):
        print(line)

# the problem will be - 'each line from the file will have a newline at the end'
# also the 'print statement will add a newline to each line'
# so there will be two '/n' including a blank line


# SEARCHING THOROUGH A FILE (fixed) - newline problem fixed
fhand = open('file/self-driving-car')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Our'):
        print(line)

# SKIPPING WITH CONTINUE
# we can conveniently skip a line by using the continue statement

fhand = open('file/self-driving-car')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# USING IN TO SELECT LINES
# we can look for a string anywhere in a line as our selection criteria
fhand = open('file/self-driving-car')
for line in fhand:
    line = line.rstrip()
    if not 'From' in line:
        continue
    print(line)

# Prompt for File Name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# BAD FILE NAMES
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
