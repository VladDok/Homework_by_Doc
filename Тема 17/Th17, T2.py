# Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution and write tests using unittest library

from faker import Faker
import JSON
import os
import unittest

name_user = os.getlogin()
direction = f'C:\\Users\\{name_user}'
os.chdir(direction)

def input(*args, **kwargs): pass
    

class Test_JSON(unittest.TestCase):
    
    def setUp(self):
        self.Faker().random.seed(1)
        self.name_book = Faker().first_name()
        self.login = self.name_book
        self.password = Faker().password()
        self.data = {
            'Ім\'я': Faker().first_name(),
            'Прізвище': Faker().last_name(),
            'Номер телефону': Faker().phone_number(),
            'Місто проживання': Faker().city()
            }
        
    def 
        
        
