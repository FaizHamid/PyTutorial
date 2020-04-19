# Chapter 3 - Conditional Executions

# If (Conditional Steps) is conditional statement. If the condition is true, then do the indented statements.
# If the condition is not true, then skip the indented statements.

# If statement
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finish')

# Nested If statement
x = 5
if x > 2:
    print('Bigger than 2')
    print('Still Bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All done!')


# MULTIWAY -
# If else statement
# Visualize Blocks

x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')

# Elif statement

x = 1
if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')
print('All done!')

# Multiway - no else
x =5
if x<2:
    print('small')
elif x<10:
    print('medium')
print('All done')