# Chapter 5.1 - LOOP IDIOMS
# what we do in loops
# Note: Even though these examples are simple, the pattern apply to all kinds of loops


# trick is knowing something about the whole loop when you are stuck writing code that only sees one entry at a time.

print('Before')
# Set some variables to initiate values.
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')
# Look for something or do something to each entry separately.
# Look at the variables.


# Variables 'largest_so_far' that contains the largest value we have seen so far.
# If the current 'number we are looking at' is larger, it is the new 'largest value we have seen so far'.
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)