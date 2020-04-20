# Chapter 5.2 - LOOP PATTERNS

# COUNTING - to 'count' how many times we execute a loop,
# we introduce a counter variable that starts at '0' and
# we add 'one to it each time through the loop'.

# Counting in a Loop
count = 0
print('Before', count)
for thing in [9, 41, 12, 3, 74, 15]:  # thing is the iteration variable
    count = count + 1
    print(count, thing)
print('After', count)

# Summing in a Loop
# to add up a value we encounter in a loop,
# we introduce a 'sum variable that start at 0' and
# we add the 'value' to the sum each time through the loop.

sum = 0
print('Before', sum)
for thing in [9, 41, 12, 3, 74, 15]:  # Thing is the iteration variable
    add = sum + thing
    print(sum, thing)

# Average in a Loop
# An 'average' just combines the counting and sum patterns and divides when the loop is done.
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:  # 'Value' is the iteration variable
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

# Filtering in a loop
# we use an if statement in the loop to catch / filter the values we are looking for.
print('Before')
for value in [9, 41, 12, 3, 74, 15]:  # 'Value' is the iteration variable
    if value > 20:
        print('Large number', value)
print('After')

# BOOLEAN VARIABLE in a Loop
# If we just want to search and 'know if a value was found', we use a 'variable' that starts at 'False' and set to 'True'
# as soon as we 'find' what we are looking for.
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

# Smallest Value
# we still have a variable that is the 'smallest' so far. The first time through the loop 'smallest' is 'None'.
# so we take the first value to be the smallest.
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)


# IS or IS NOT Operators
# Python has a 'IS' operator that can be used in logical expressions.
# implies 'IS THE SAME AS' or similar to, but stronger than ==
# 'IS NOT' also is a logical operator.

