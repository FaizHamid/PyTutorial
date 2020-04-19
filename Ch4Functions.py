# Chapter 4 - Python Functions
# Function Types - there are two types of function in Python.

# (1) Built-in functions: that are provided as part of Python, like print(), input(), type(), float(), int()...
# we treat the built-in function names as "new" reserved words (i.e. we avoid them in variable names)

# (2) Stored and reused Function: that we define ourselves and then reuse..


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
