# =============================================================================
# Doggy age
# 
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() 
# which takes values for a dog’s age. Then create a method `human_age` which 
# returns the dog’s age in human equivalent.
# 
# =============================================================================
class Dog():
    '''Для створення собаки та
    можливістю конвертувати у людський вік.'''
    
    age_factor = 7
    
    def __init__(self, dog_age, dog_weight):
        if type(dog_age) == str or type(dog_weight) == str:
            dog_age = int(dog_age)
            dog_weight = int(dog_weight) 
        self.dog_age = dog_age
        self.dog_weight = dog_weight
        if self.dog_age <= 0 or self.dog_weight <= 0:
            raise TypeError('Вік і вага не можуть бути від\'ємними числами.')
    
    def human_age(self):
        while True:
            if type(self.dog_age) == int:
                if self.dog_age == 1:
                        age = 15
                elif self.dog_age == 2:
                        age = 24
                else:
                    if self.dog_weight < 12:
                        age = 24 + (self.dog_age - 2) * 4
                    elif self.dog_weight < 25:
                        if self.dog_age == range(3, 7):
                            age = 24 + (self.dog_age - 2) * 4
                        else: 
                            list_ages = [x for x in list(range(self.dog_age + 1)) if x > 6]
                            pairs = len([x for x in list_ages if x%2 == 0])
                            nonpairs = len([x for x in list_ages if x%2 == 1])
                            age = 42 + pairs * 4 + nonpairs * 5
                    else:
                        if self.dog_age in range(3, 6):
                            age = 24 + (self.dog_age - 2) * 4
                        elif self.dog_age in range(6, 11):
                            if self.dog_age == 6:
                                age = 45
                            else:
                                age = 45 + 5 * (self.dog_age - 6)
                        elif self.dog_age == 11:
                            age = 72
                        elif self.dog_age == 12:
                            age = 77
                        else:
                            age = 77 + 5 * (self.dog_age - 12)
                return age
            else:
                self.dog_age = int(round(self.dog_age))
                continue
            
            
dog_1 = Dog(3, 10)

print(dog_1.human_age())
                
        