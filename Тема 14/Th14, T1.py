# =============================================================================
# Write a decorator that prints a function with arguments passed to it.
# 
# NOTE! It should print the function, not the result of its execution!
# 
# For example:
# 
#  "add called with 4, 5"
# 
# ```
# 
# def logger(func):
# 
#     pass
# 
#  
# 
# @logger
# 
# def add(x, y):
# 
#     return x + y
# 
#  
# 
# @logger
# 
# def square_all(*args):
# 
#     return [arg ** 2 for arg in args]
# 
# ```
# =============================================================================

from functools import wraps
from inspect import getcallargs

def logger(func):
    @wraps(func)
    def wrap(*args):
        print(func.__name__ + ' called with ' + str(getcallargs(func, *args)) + '.')
    return wrap
      
@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == '__main__':
    add(4, 5)
    print('')
    square_all(1, 2, 3)   

