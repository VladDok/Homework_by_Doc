# The greeting program.

# Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

#      “Good day <name>! <day> is a perfect day to learn some python.”
 

# Note that <name> and <day> are predefined variables in source code.

# An additional bonus will be to use different string formatting methods for constructing result string.

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
