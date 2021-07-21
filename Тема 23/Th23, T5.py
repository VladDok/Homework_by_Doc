def sum_of_digits(digits_string: str) -> int:
    """Підсумовує усі числа строки та повертає результат цілим числом."""
    
    if not digits_string.isdigit():
        raise ValueError('input string must be digit string')
    
    if len(digits_string) == 1:
        return int(digits_string)
    
    else:
        return int(digits_string[0]) + sum_of_digits(digits_string[1:])
    
    
print(sum_of_digits('26') == 8)
print(sum_of_digits('test'))

