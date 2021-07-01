# =============================================================================
# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
# 
# Email validations:
# 
# https://help.xmatters.com/ondemand/trial/valid_email_format.htm 
# 
# https://en.wikipedia.org/wiki/Email_address 
# =============================================================================

class Address:
       
    def validate(address):
        address_parts = address.split('@')
        if len(address_parts) == 1:
            raise TypeError('Почта повинна містити префікс "@".')
        elif len(address_parts) > 2:
            raise TypeError('Почта повинна містити тільки один префікс "@" перед доменои почти.')
        else:
            if address_parts[0].endswith('.') or address_parts[0].endswith('-'):
                raise TypeError('Перед "@" неможе бути "." чи "-".')
            for char in address_parts[0]:
                if char.isalpha() or char == '.' or char == '-' or char == '_' or char.isdigit():
                    continue
                else:
                    raise TypeError('Префікс адреси повинен містити букви (a-z), цифри, символи підкреслення, крапки та тире.')
            else:
                domain_parts = address_parts[1].split('.')
                if len(domain_parts) > 2:
                    raise TypeError('Домен повинен містити тільки дві частини розділених крапкою (example, gmail.com).')
                elif len(domain_parts[-1]) < 2:
                    raise TypeError('Кінець домену повинен містити не менше 2 символів.')
                elif domain_parts[-1].isalpha() == False:
                    raise TypeError('Кінець домену неповинен містити числа.')
                else:
                    for part in domain_parts:
                        for char in part:
                            if char.isalpha() or char == '-' or char.isdigit():
                                continue
                            else:
                                raise TypeError('Домен повинен містити тільки букви, цифри, тире.')
    
    def __init__(self, address):
        Address.validate(address)
        self.address = address
        
    def __str__(self):
        return f'Твоя електронна адреса: {self.address}.'
    

my_address = Address('kuzniak-vl@gmail.com')
print(my_address)
                  
            

