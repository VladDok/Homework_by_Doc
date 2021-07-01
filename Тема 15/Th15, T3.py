# =============================================================================
# Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's possible):
# 
# methods:
# 
# to_int
# 
# to_str
# 
# to_bool
# 
# to_float
# 
#  
# 
# Don't forget to use @wraps
# 
# ```
# 
# class TypeDecorators:
# 
#     pass
# 
#  
# 
# @TypeDecorators.to_int
# 
# def do_nothing(string: str):
# 
#     return string
# 
#  
# 
# @TypeDecorators.to_bool
# 
# def do_something(string: str):
# 
#     return string
# 
#  
# 
# assert do_nothing('25') == 25
# 
# assert do_something('True') is True
# 
# ```
# =============================================================================

class MethodError(Exception):
    
    def __str__(self):
        return 'Даний метод неможна використовувати до даної функції з теперішнім аргументом.'


class TypeDecorators:
    
    def to_int(func):
        def wrap(*args, **kwargs):
            if func(*args, *kwargs).isdigit():
                return int(func(*args, *kwargs))
            else:
                raise MethodError
        return wrap
    
    def to_str(func):
        def wrap(*args, **kwargs):
            if func(*args, *kwargs).isalnum():
                return str(func(*args, *kwargs))
            else:
                raise MethodError
        return wrap
    
    def to_float(func):
        def wrap(*args, **kwargs):
            if func(*args, *kwargs).isdigit():
                return float(func(*args, *kwargs))
            else:
                raise MethodError
        return wrap
    
    def to_bool(func):
        def wrap(*args, **kwargs):
            return bool(func(*args, *kwargs))
        return wrap


@TypeDecorators.to_int
def do_nothing(string):
    return string

@TypeDecorators.to_bool
def do_something(string):
    return string


print(do_nothing('25'))
print(do_something('Python'))
print(do_nothing('Python'))

