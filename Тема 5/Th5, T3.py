# Make a list that contains all integers from 1 to 100, 
# then find all integers from the list that are divisible 
# by 7 but not a multiple of 5, and store them 
# in a separate list. Finally, print the list.

# Constraint: use only while loop for iteration

# My solution

common_list = list(range(1, 101))
new_list = []

i = 0
while i < len(common_list) - 1:
    integer = common_list[i]
    if integer % 7 == 0 and integer % 5 != 0:
        new_list.append(integer)
        i += 1
    else:
        i += 1

print('The result is:', new_list)
    

