# Chapter 4 - Python Functions
# Function Types - there are two types of function in Python.

# (1) Built-in functions: that are provided as part of Python, like print(), input(), type(), float(), int()...
# we treat the built-in function names as "new" reserved words (i.e. we avoid them in variable names)

# (2) Stored and reused Function: that we define ourselves and then reuse.. (our own functions...)


def thing():
    print('Hello')
    print('Fun')


thing()
print('Zip')
thing()


# Function Definition
# (a) in Python a 'function' is some reusable codes that take 'argument(s)' as input, does some computation, and then returns the result.
# (b) we define the 'function' using the 'def' reserved word
# (c) we call/invoke the 'function' by using the function name, parentheses, and 'arguments' in an exception

# Building our own 'Functions'
# we crate a new function with the 'def' keyword followed by optional parameters in parentheses
# we indent the body of the function
# this defines the function but does not execute the body of the function

# print_lyrics function defined
def print_lyrics():
    print_lyrics("I am a lumberjack, and I'm okay")
    print_lyrics('I sleep all night, and I work all day')


# Definitions and Uses
# Once we have defined a function, we can call (or invoke) it as many times as we like
# This is a store and reuse pattern

# ARGUMENTS
# An 'argument' is a value we pass into the function as its input when we call the function.
# We use 'arguments' so we can direct the function to do different kinds of work when we call it at different times.
# We put the 'arguments' in parentheses after the name of the function.

big = max('Hello World')  # here Hello World is an argument


# PARAMETERS
# A parameter is a variable which we use in the function definition. It is a "handle" that allows the code in the
# function to access the arguments for a particular function invocation.

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


# RETURN values
# Often a function will take its arguments, do some computation, and 'return' a value to be used as the value of the
# function call in the calling expression. The 'return' is used for this..

def greet():
    return "Hello"


print(greet(), 'Glenn')
print(greet(), "Sally")


# A fruitful 'function' is one that produces a result "or return value"
# The return statement ends the function execution and "sends back" the result of the function

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet('en'), 'Glenn')
print(greet('es'), "Sally")
print(greet('fr'), "Michael")


# we can define more than one 'parameter' in the 'function' 'definition'.
# we simply add more 'arguments' when we call the 'function'.
# we match the number and order of arguments and parameters.

def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)
print(x)

# TO FUNCTION OR NOT TO FUNCTION
# organize your code into "paragraphs" - capture a complete thought and "name it"
# Don't repeat itself - make it work once and then reuse it
# If something gets too long or complex, break it up into logical chunks and put those chunks in functions.
# Make a library of common stuff that you do over and over - perhaps share this with your friends.
