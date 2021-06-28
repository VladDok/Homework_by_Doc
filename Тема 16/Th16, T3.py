class Check_on_type:
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        print(owner)
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if (type(value) != list) and (type(value) != str):
            raise TypeError('Type this object can\'t useing.')   
        instance.__dict__[self.name] = value    

class MyItter:
    
    obj = Check_on_type('obj')
    
    def __init__(self, obj):
        self.subject = obj
        self.index = 0
        
    def __iter__(self):
        return self
     
    def __next__(self):
        while self.index < len(self.subject):
            result = self.subject[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
    def __getitem__(self, index):
        return self.subject[index]
        

if __name__ == '__main__':
    obj = MyItter('asdfg')
    print(obj[0])
    for i in obj:
        print('-'*30)
        print(i)


