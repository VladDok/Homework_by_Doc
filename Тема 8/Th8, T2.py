# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided 
# by b, construct a try-except block which raises an exception if the two 
# values given by the input function were not numbers, and if value b was 
# zero (cannot divide by zero).   

def division_two_numbers():
    """ This function division square of a on b """
    while True:
        try:
            a = int(input('Write the number called a: '))
            b = int(input('Write the number called b: '))
            total = a**2 / b
        except ZeroDivisionError:
            print('\nNumber b can\'t be 0. Try again.')
            continue
        except ValueError as error:
            print(f'\nHappened next error: {error.args} \nCheck your error.')
            continue
        else:
            print(f'\nYour result: {total}')
            break

                  
division_two_numbers()  
