def reverse(input_str: str) -> str:
    """Фукнція повертає перевернуту строку."""

    if len(input_str) == 0:
        return ''
    
    elif len(input_str) == 1:
        return input_str
    
    else:
        return input_str[-1] + reverse(input_str[1:-1]) + input_str[0]
    
    
print(reverse("hello") == "olleh")
print(reverse("o") == "o")
    
