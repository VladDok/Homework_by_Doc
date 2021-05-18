#create variables
name = 'Vlad'
day = 'Thuersday'

#the first method
print(f'Good day {name}! {day} is a perfect day to learn some Python.')

#the second method
print('Good day {0}! {1} is a perfect day to learn some Python.'.format(name, day))

#the third method
print('Good day %s! %s is a perfect day to learn some Python.' % (name, day))
