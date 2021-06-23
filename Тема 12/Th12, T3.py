# =============================================================================
# Fraction
# 
# ‎Створити клас Fraction, який буде представляти всю базову арифметичну логіку дробів (+, -, /, *) з відповідною перевіркою та обробкою помилок‎
# 
# ```
# 
# class Fraction:
# 
# pass
# 
# x = Fraction(1/2)
# 
# y = Fraction(1/4)
# 
# x + y == Fraction(3/4)
# 
# ```
# =============================================================================

import sys

class Fraction:
    
    def __init__(self, number):
        assert(type(number) != str), 'Використовуйте тільки числа.'
        self.number = number
    
    def __add__(self, other):
        return self.number + other.number
    
    def __sub__(self, other):
        return self.number - other.number
    
    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        try:   
            return self.number/other.number
        except ZeroDivisionError:
            print('На нуль ділити не можна!')
        finally:
            sys.exit()
        
    def __eq__(self, other):
        return print(self.number == other)
    
    def __str__(self):
        return f'{self.number}'
        
    def __repr__(self):
        return f'{self.number}'


n = Fraction(5)
m = Fraction(6)

print(m+n)
print(m-n)
print(m*n)
print(m/n)

x = Fraction(1/2)
y = Fraction(1/4)
x + y == Fraction(3/4)


