# =============================================================================
# A Person class
# 
# Make a class called Person. Make the __init__() method take firstname, 
# lastname, and age as parameters and add them as attributes. Make another 
# method called talk() which makes prints a greeting from the person containing, 
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
# =============================================================================

class Person():
    '''Створює особу, яка здатна представлятися.'''
    
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        if type(age) is int and age>0:
            self.age = age
        else:
            raise TypeError('Зверніть увагу на вік.')
        
    def talk(self):
        return ('\nПривіт, мене звати ' + self.firstname.title() + ' '
        + self.lastname.title() + ' і мені ' + str(self.age) + '.')


person = Person('john', 'johson', 34)

person.talk()


