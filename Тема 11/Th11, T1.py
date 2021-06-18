# =============================================================================
# School
# 
# Make a class structure in python representing people at school. Make a base 
# class called Person, a class called Student, and another one called Teacher. 
# Try to find as many methods and attributes as you can which belong to different 
# classes, and keep in mind which are common and which are not. For example, 
# the name should be a Person attribute, while salary should only be available 
# to the teacher. 
# =============================================================================

class Person():
    '''Клас визначає особистість.'''
    
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)
        self.sex = sex
            

class Teacher(Person):
    '''Клас для опису вчителя.'''
    
    def __init__(self, first_name, last_name, age, sex, teach_age, subject, status):
        super().__init__(first_name, last_name, age, sex)
        self.teach_age = teach_age
        self.subject = subject
        self.status = status
        
    def salary(self, sal=1500):
        '''Нарахування зарплати залежно від кількості років викладання.'''
        if self.teach_age < 10:
            print(self.first_name.title(), self.last_name.title(), f'earn {sal} dollars.')
        elif self.teach_age < 20:
            print(self.first_name.title(), self.last_name.title(), f'earn {sal+500} dollars.')
        else:
            print(self.first_name.title(), self.last_name.title(), f'earn {sal+1000} dollars.')

    def amount_groups(self):
        '''Кількість груп залежно від статусу.'''
        if self.status == 'aspirant':
            print(self.first_name.title(), self.last_name.title(), 'has 3 groups.')
        elif self.status == 'docent':
            print(self.first_name.title(), self.last_name.title(), 'has 8 groups.')
        elif self.status == 'proffesor':
            print(self.first_name.title(), self.last_name.title(), 'has 12 groups.')
            
    def faculty_for_teach(self):
        '''Визначення факультету, де викладач працює.'''
        print(self.first_name.title(), self.last_name.title(), 'is teacher in faculty of', self.subject.title() + '.')
        
    

class Student(Person):
    '''Клас для опису студента'''
    
    def __init__(self, first_name, last_name, age, sex, city, 
university, faculty, course, group, status):
        super().__init__(first_name, last_name, age, sex)
        self.city = city
        self.university = university
        self.faculty = faculty
        self.course = str(course)
        self.group = str(group)
        self.status = status
        
        
    def stependium(self):
        '''Отримання стипендії.'''
        if self.status == 'good':
            print(self.first_name.title(), self.last_name.title(), 'has 300 dollars.')
        elif self.status == 'excellent':
            print(self.first_name.title(), self.last_name.title(), 'has 500 dollars.')
        else:
            print(self.first_name.title(), self.last_name.title(), 'не отримує стипендії.')

