# =============================================================================
# Mathematician
# 
# Implement a class Mathematician which is a helper class for doing math operations on lists
# 
# The class doesn't take any attributes and only has methods:
# 
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
# ```
# 
# class Mathematician:
# 
#     pass
# 
#  
# 
# m = Mathematician()
# 
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# 
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# 
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
# =============================================================================

class Square_nums():
    '''Для взяття квадрату кожного числа зі списку.'''
    
    def square_nums(self, list):
        list = [num**2 for num in list]
        return list
            
    
class Remove_possitives():
    '''Для видалення зі списку позитивних чисел.'''
    
    def remove_possitives(self, list):
        list = [num for num in list if num<0]
        return list
    
    
class Filter_lips():
    '''Бере список років і видаляє, які не є високоснимироками.'''
    
    def filter_lips(self, list):
        list = [year for year in list if (year%4 == 0) and not(year%100 == 0)]
        return list
    

class Mathematician(Square_nums, Remove_possitives, Filter_lips):
    '''Клас, який об\'єднує усі операції.'''
    pass


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16])
print(m.remove_possitives([26, -11, -8, 13, -90]) == [-11, -8, -90])
print(m.filter_lips([2001, 1884, 1995, 2003, 2020]) == [1884, 2020])
    
    
    
    
    