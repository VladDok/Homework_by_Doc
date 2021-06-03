# Write a function called oops that explicitly raises an IndexError exception 
# when called. Then write another function that calls oops inside a try/except 
# state­ment to catch the error. What happens if you change oops to 
# raise KeyError instead of IndexError?

# 1 function which call except

def oops():
    raise IndexError('This function called IndexError')

# 3 function which don't intercept except

# def oops():
#    raise KeyError('For check check() function')

# 2 function which intercept except

def check():
    try:
        oops()
    except IndexError:
        print('Except has intercepted successful!')


check()
