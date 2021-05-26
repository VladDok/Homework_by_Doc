# String manipulation

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

# Sample String: 'helloworld'

# Expected Result : 'held'

# Sample String: 'my'

# Expected Result : 'mymy'

# Sample String: ' x'

# Expected Result: Empty String

# Tips:

# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters

# My solution

answer = 'yes'
i = 0

print('Hello. Please, write your string.')

while answer.lower() == 'yes':
    s = input('Sample String: ')
    ind = 0
    while i < len(s):
        if s[i].isdigit() == True:
            print('Don\'t use number!')
            ind = 1
            break
        i += 1
    
    if ind == 1:
        continue
    else:
        if len(s) < 4:
            print('')
        else:
            print(f'Expected Result: {s[:2] + s[-2:]}')
    
        answer = input('Try again? Change \'yes\' or \'no\'?\n')
        if answer.lower() == 'yes':
            continue
        elif answer.lower() == 'no':
            print('\nBye!')
            break
        else:
            answer = input('No! Change \'yes\' or \'no\'?\n')
        
            while answer.lower() not in ('yes', 'no'):
                answer = input('No! Change \'yes\' or \'no\'?\n')
            else:    
                if answer.lower() == 'no': 
                    print('\nBye!')
                    break

        


         
                    
                    
