# Chapter 7 - Reading Files

# OPENING A FILE
# before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file
# this is done with the 'open()' function
# open() returns a "file handle" - a variable used to perform operations on the file
# Similar to "File -> Open" in a Word Processor

# USING OPEN
# handle = open(filename, mode)
# fhand = open('mbox.txt', 'r')
# returns a handle use to manipulate the file
# filename is a string
# mode is option and should be 'r' if we are planning to read the file and 'w' if we want to write the file

