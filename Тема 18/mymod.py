# =============================================================================
# Basics, import, work with os module
# 
# Write a program that counts lines and characters in a file (similar to `wc` Unix-utility, for additional info about it follow the link: https://www.geeksforgeeks.org/wc-command-linux-examples/ or in case you have macOS or Linux - just call manual for this utility via command: `man wc`).
# 
#  Create a Python module called `mymod.py`, which has three functions:
# 
# count_lines(name) function that reads an input file and counts the number of lines in it (hint: file.readlines() does most of the work for you, and `len` does the rest) 
# count_chars(name) function that reads an input file and counts the number of characters in it (hint: file.read() returns a single string)
# test(name) function that calls both counting functions with a given input file­name. Such a filename generally might be passed-in, hard-coded, input with raw_input, or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
# All three `mymod.py` functions should expect a filename string to be passed in. 
# 
# Test your module interactively, using import and name qualification to fetch your exports. 
# 
# Does your PYTHONPATH need to include the directory where you created mymod.py?
# 
# Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice; if you’re feeling ambitious, you may be able to improve this by passing an open file object into the two count functions (hint: file.seek(0) is a file rewind).
# =============================================================================

import os

print(f'Доброго дня шановний користувачу. Дані методи працюватимуть на даний момент\n\
з файлами, які можна знайти по даній директорії: {os.getcwd()}.\n')

name = input('Уведіть повну назву файлу (наприклад, file.txt): ')

if name in os.listdir():
    def count_lines(name):
        '''Reads an input file and counts the number of lines in it'''
        
        with open(name) as file:
            lines = file.readlines()
            lenght = len(lines)
            return f'Amount of lines is {lenght}.'
        
    def count_chars(name):
        '''Reads an input file and counts the number of characters in it'''
        
        with open(name) as file:
            lenght_with_space = 0
            lenght_without_space = 0
            line = file.readline()
            while line:
                line = line[:-2]
                lenght_with_space += len(line) 
                line_with_no_space = line.split()
                for line in line_with_no_space:
                    lenght_without_space += len(line)
                line = file.readline()
            else:
                return f'Lenght with space: {lenght_with_space}.\n\
Lenght without space: {lenght_without_space}.'
    
    def test(name):
        '''Calls both counting functions with a given input file­name'''
        
        list_functions = [count_lines(name), count_chars(name)]
        
        for func in list_functions:
            print(func)
        
        return ''
    
    print(count_lines(name))
    print(count_chars(name))
    print('-'*20)
    print(test(name))
else:
    raise FileNotFoundError('Уведеного імені файлу неіснує в даній директорії.\n\
Перевірте його наявність або змініть директорію.')
        
                 
    
