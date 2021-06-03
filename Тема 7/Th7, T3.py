# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic 
# operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
# and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42  

def make_operation(operator, *args):
    total = args[0]
    i = 1
    while i < len(args):
        if type(args[i]) == str:
            print('Don\'t use string!')
            return None
        else:
            if operator == '+':
                total += args[i]
                i += 1
            elif operator == '-':
                total -= args[i]
                i += 1
            elif operator == '*':
                total *= args[i]
                i += 1
            else:
                print('Such operator does not exist. Please, try again!')
                continue
    return total


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
