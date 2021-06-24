# =============================================================================
# Write a Python program to access a function inside a function 
# (Tips: use function, which returns another function)
# =============================================================================

def print_smth(r):
    def print_up(word):
        print(word.upper())
    def print_down(word):
        print(word.lower())
    def default():
        print('Даного режиму неіснує.')
    dictionary = {'up':print_up, 'down':print_down}
    return dictionary.get(r, default)
        
        
func =  print_smth('up')
func('Hello')
    

