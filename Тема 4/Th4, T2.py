# The birthday greeting program.

# Write a program that takes your name as input, and then your age as input and greets you with the following:

# “Hello <name>, on your next birthday you’ll be <age+1> years”   

# My solution

while True:
    answer_1 = input('What is your name?\n').capitalize()
    i = 0
    ind = 0
    while i < len(answer_1):      
        if answer_1[i].isdigit() == True:
            ind = 1
            print('jkjkj')
            break
        else:
            i += 1
    if ind == 1:
        continue
    else:
        break
    
while True:
    answer_2 = input('How old are you?\n')
    i = 0
    ind = 0
    while i < len(answer_2):    
        if answer_2[i].isalpha() == True:
            ind = 1
            print('sasas')
            break
        else:
            i += 1
    if ind == 1:
        continue
    else:
        break

print(f'Hello {answer_1}, on your next birthday you’ll be {int(answer_2) + 1} years')

        
    
