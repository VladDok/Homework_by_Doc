# Exclusive common numbers.

# Generate 2 lists with the length of 10 with random 
# integers from 1 to 10, and make a third list containing 
# the common integers between the 2 initial lists 
# without any duplicates.

# Constraints: use only while loop and random module to generate numbers

# My solution

from random import randint

first_random_list = []
second_random_list = []

i = 0
while i < 11:
    random_number_for_first_list = randint(1, 10)
    first_random_list.append(random_number_for_first_list)
    i += 1
    
i = 0
while i < 11:
    random_number_for_second_list = randint(1, 10)
    second_random_list.append(random_number_for_second_list)
    i += 1

common_random_list = first_random_list + second_random_list
original_random_list = list(set(common_random_list))

print('The result is:', original_random_list)
