from typing import Optional, Mapping

def to_power(x: Optional[Mapping[int, float]], exp: int) -> Optional[Mapping[int, float]]:
    """Функція для взяття степеня числа х."""
    
    if exp == 1:
        return x
    elif exp > 1:
        return (x * to_power(x, exp-1))
    else:
        raise ValueError('This function works only with exp > 0.')


print(to_power(2, 3) == 8)
print(to_power(3.5, 2) == 12.25)

print(to_power(2, -1))
    
        
        

    
        
        
        

