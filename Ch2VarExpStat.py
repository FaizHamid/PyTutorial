# Chapter 2 - Variables, Expressions, and Statements

# CONSTANTS
# Fixed values such as numbers, letters, and strings, are called "constants" because their values does not change
# Numeric constants are as you expect
# String constants use single quotes (') or double quotes (")

print(123)

print(98.6)

print("Hello World!")

# VARIABLES - are named place in the memory where a programmer can store data and later retrieve the data using the variable "name".

# Programmers get to choose the variables. You can change the contents of a variable in the later statement.

x = 12.2
y = 14

# MNEMONIC VARIABLE NAMES:
# Since we programmers are given a choice in how we choose our variable names, there is a bit of best practices".
# We name variables to help us remember what we intend to store in them ("mnumonic" = "memory aid").
# Well-named variables often "sound" so good that they must be key words.

# Long and inconvenient variables, and easy to make mistakes
xlq3z9ocd = 35.0
xlq3z9afd = 12.5
xlq3p9afd = xlq3z9ocd * xlq3z9afd
print(xlq3p9afd)

# Short and convenient variables, but not clear what these variables means
a = 35.0
b = 12.50
c = a * b
print(c)

# Mnemonic variables, very easy to understand
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

# TYPE MATTERS
eee = "Hello World"
type(eee)
