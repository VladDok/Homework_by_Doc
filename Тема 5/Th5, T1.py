# The greatest number

# Write a Python program to get the largest number 
# from a list of random numbers with the length of 10

# Constraints: use only while loop and random module 
# to generate numbers

# My solution

from random import randint

list_of_numbers = []

i = 0
while i < 10:
    random_number = randint(1, 100)
    list_of_numbers.append(random_number)
    i += 1
    
max_number = max(list_of_numbers)
list_of_number_for_cycle = list_of_numbers.copy()
max_number_for_cycle = max_number
amount_of_max_number = 1

while True:
    list_of_number_for_cycle.remove(max_number_for_cycle)
    max_number_for_cycle = max(list_of_number_for_cycle)
    if max_number_for_cycle == max_number:
        amount_of_max_number += 1
        continue
    else:
        break

print('Max number in random list is:', max_number, '\n' +
      'It amount is:', amount_of_max_number)
    

