def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """Перевіряє строку на властивість паліндрому."""
    
    if len(looking_str) == 1 or len(looking_str) == 0:
        return True
    
    elif len(looking_str) > 1:
        if looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        
        else:
            return False
        
        
print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))
print(is_palindrome('asdfsa'))
        
    

