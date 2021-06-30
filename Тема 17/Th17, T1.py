# Imports practice

# Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.

from faker import Faker
import unittest
from test_class import Person


class TestClass(unittest.TestCase):
    
    def setUp(self): 
        self.fake = Faker()
        self.fake.random.seed(1)
        self.fake_first_name = self.fake.first_name()
        self.fake_last_name = self.fake.last_name()
        self.fake_age = self.fake.random_number(2)
        self.person = Person(
            firstname = self.fake_first_name,
            lastname = self.fake_last_name,
            age = self.fake_age
            ) 
    
    def test_instance(self):
        self.assertIsInstance(self.person, Person)
    
    def test_first_name(self):
        self.assertEqual(self.person.firstname, self.fake_first_name)
        
    def test_last_name(self):
        self.assertEqual(self.person.lastname, self.fake_last_name)

    def test_age(self):
        self.assertEqual(self.person.age, self.fake_age)
        
    def test_talk(self):
        self.assertEqual('\nПривіт, мене звати ' + self.fake_first_name.title() + ' '
        + self.fake_last_name.title() + ' і мені ' + str(self.fake_age) + '.', self.person.talk())
        
        
unittest.main()
        

