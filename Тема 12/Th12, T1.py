# =============================================================================
# Method overloading.
# 
# Create a base class named Animal with a method called talk and then create two 
# subclasses: Dog and Cat, and make their own implementation of the method talk 
# be different. For instance, Dog’s can be to print ‘woof woof’, while 
# Cat’s can be to print ‘meow’.
# 
# Also, create a simple generic function, which takes as input instance of a Cat 
# or Dog classes and performs talk method on input parameter.  
# =============================================================================

class Animal:
    'Тварини можуть вітатися'
    
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        pass
    
    
class Cat(Animal):
    'Котик мявчить'
    
    def __init__(self, name):
        super().__init__(name)
    
    def say_hello(self):
        return 'Meow'
    
    
class Dog(Animal):
    'Собака гавкає'
    
    def __init__(self, name):
        super().__init__(name)
    
    def say_hello(self):
        return 'Woof-woof'
    
    
def print_hello(animal):
    print(animal.name, 'say:', animal.say_hello())


cat = Cat('Marcis')
dog = Dog('Rullfe')

print_hello(cat)
print_hello(dog)
    
    

    

    
    
    
    

        

