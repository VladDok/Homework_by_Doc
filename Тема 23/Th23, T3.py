def mult(a: int, n: int) -> int:
    """Дана функція виконує дію множення між двома позитивними цілими числамию"""
    
    if n < 0 or a < 0:
        raise ValueError('This function works only with postive integers')
    
    if n == 0:
        return 0
    
    elif n == 1:
        return a
    
    else:
        return (a + mult(a, n-1))
 
    
print(mult(2, 4) == 8)
print(mult(2, 0) == 0)
print(mult(2, -4))

