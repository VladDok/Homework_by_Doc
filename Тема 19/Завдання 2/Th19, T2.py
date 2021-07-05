import unittest
from faker import Faker
from class_example import MyManager


def print(*args):
    return args


class TestClass(unittest.TestCase):
    
    def __setUp__(self):
        self.seed = Faker().random.seed(1)
        self.first_name = Faker().first_name()
        self.last_name = Faker().last_name()
        self.person = MyManager(
            first_name = self.first_name,
            last_name = self.last_name,
            )       

    def test_mymaneger_creation(self):
        self.assertIsInstance(self.person, MyManager)
    
    def test_name(self):
        self.assertEqual(Faker().first_name(), self.person.first_name)
        
    def test_surname(self):
        self.assertEqual(Faker().last_name(), self.person.last_name)
        
    def test_get_val(self):
        start_counter = MyManager.counter
        finish_counter = MyManager.get_value_counter()
        self.assertEqual(finish_counter, start_counter+1)
        
    def test_enter(self):
        return self.person.__enter__()
        

unittest.main()
        