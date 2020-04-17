# Chapter 5

# Like a recipe or installation instruction, a program is a sequence of steps to be done in orders.
# Some steps are conditional - they may be skipped.
# Sometimes a steps or a group of steps is to be repeated.
# Sometimes we store a set of steps to be used over and over as needed several places throughout the program.

x = 2
print(x)
x = x + 2
print(x)

# When a program is running, it flows from one step to the next. As programmers, we set up "paths" for program to follow.

# Conditional Steps

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finish')

