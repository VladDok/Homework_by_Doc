def sum_of_numbers(x, y, z):
    '''Function as experimental'''
    return x+y+z

def check_amount_var(func):
    try:
        func()
        print('Amount of variables = 0' )
    except TypeError as msg:
        amount = filter(lambda i: i.isdigit(), msg) 
        print('Amount of variables = ' + amount)
    
Function.__class__