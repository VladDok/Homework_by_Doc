class MyManager:
    ''''''
    counter = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_value_counter():
        MyManager.counter += 1
        return MyManager.counter
    
    def __enter__(self):
        MyManager.get_value_counter()
        print(f'Your {self.first_name} and your {self.last_name} are writen {MyManager.counter}.')
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('This realized is a finishing.')
        return None
    
    
with MyManager('Vlad', 'Kuzniak') as man:
    print('-'*40)

print('')    

with MyManager('Vlad', 'Kuzniak') as man:
    print('-'*40)

print('')
    
with MyManager('Vlad', 'Kuzniak') as man:
    print('-'*40)

print('')
    
with MyManager('Vlad', 'Kuzniak') as man:
    print('-'*40)

print('')
    
with MyManager('Vlad', 'Kuzniak') as man:
    print('-'*40)
        
        
        


