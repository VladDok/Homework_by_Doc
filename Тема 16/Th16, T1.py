# =============================================================================
# Create your own implementation of a built-in function enumerate, named `with_index`, 
# which takes two parameters: `iterable` and `start`, default is 0. Tips: see the 
# documentation for the enumerate function.
# =============================================================================

def with_index(iterable, start=0):
    if type(iterable) is list or type(iterable) is str or  type(iterable) is tuple:
        i = 0
        while i < len(iterable):
            yield (start, iterable[i])
            start += 1
            i += 1
    elif type(iterable) is dict:
        list_keys = [key for key in iterable.keys()]
        i = 0
        while i < len(iterable):
            yield (start, list_keys[i])
            start += 1
            i += 1
    elif type(iterable) is set:
        i = 0
        new_iterable = iterable
        while i < len(iterable):
            yield (start, new_iterable.pop())
            start += 1
    else:
        raise TypeError('Дана функція непідтримує тип змінної.')
        

for i in with_index({3, 4, 5, 6}, 8):
    print(i)        
        
        