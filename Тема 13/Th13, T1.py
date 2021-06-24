#Write a Python program to detect the number of local variables declared in a function.

def sum_of_numbers(x, y, z, a):
    '''Function as experimental'''
    return x+y+z

def check_amount_var(func):
    print(f'Amount of variables is {func.__code__.co_argcount}' ) 
    print(f'They have names: {[name for name in func.__code__.co_varnames]}')
    
    
