# Manipulate strings.

# Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.

# My solution

#create variables
name = 'Vlad'
day = 'Thuersday'

#the first method
print(f'Good day {name}! {day} is a perfect day to learn some Python.')

#the second method
print('Good day {0}! {1} is a perfect day to learn some Python.'.format(name, day))

#the third method
print('Good day %s! %s is a perfect day to learn some Python.' % (name, day))
