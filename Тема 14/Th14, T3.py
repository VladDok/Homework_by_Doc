# =============================================================================
# Write a decorator `arg_rules` that validates arguments passed to the function.
# 
# A decorator should take 3 arguments:
# 
# max_length: 15
# 
# type_: str
# 
# contains: [] - list of symbols that an argument should contain
# 
# If some of the rules' checks returns False, the function should return False 
# and print the reason it failed; otherwise, return the result.
# 
# ```
# 
# def arg_rules(type_: type, max_length: int, contains: list):
# 
#     pass
# 
#  
# 
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# 
# def create_slogan(name: str) -> str:
# 
#     return f"{name} drinks pepsi in his brand new BMW!"
# 
#  
# 
# assert create_slogan('johndoe05@gmail.com') is False
# 
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
# 
# ```
# =============================================================================

from functools import wraps

def arg_rules(func, type_=str, max_lenght=15, contains=['05', '@']):
    @wraps(func)
    def wrap(word):
        if type(word) is not type_:
            return False, 'Аргумент не є строкового типу.'
        elif len(word) > max_lenght:
            return False, 'Довжина слова більше 15 знаків'
        else:
            for item in contains:
                if item not in word:
                    return False, 'Слово не містить ключових слів.'
            else:
                return func(word)     
    return wrap    

@arg_rules
def create_slogan(word):
    return f'{word} drinks pepsi in his brand new BMW!'


if __name__ == '__main__':
    print(create_slogan('Nasty05@'))

