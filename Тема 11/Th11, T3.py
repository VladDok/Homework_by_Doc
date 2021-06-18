# =============================================================================
# Write a class Product that has three attributes:
# 
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate 
# with all products in the store. All methods, in case they can’t perform its action,
#  should raise ValueError with appropriate error information.
# 
# Tips: Use aggregation/composition concepts while implementing the ProductStore 
# class. You can also implement additional classes to operate on a certain type of 
# product, etc.
# 
# Also, the ProductStore class must have the following methods:
# 
# add(product, amount) - adds a specified quantity of a single product with a predefined 
# price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for 
# all products specified by input identifiers (type or name). The discount must be 
# specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from 
# the store if available, in other case raises an error. It also increments income 
# if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of 
# items in the store.
# ```
# 
# class Product:
# 
#     pass
# 
# class ProductStore:
# 
# pass
# 
# p = Product('Sport', 'Football T-Shirt', 100)
# 
# p2 = Product(Food, 'Ramen, 1.5)
# 
# s = ProductStore()
# 
# s.add(p, 10)
# 
# s.add(p2, 300)
# 
# s.sell(‘Ramen’, 10)
# 
# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
# =============================================================================

class Product:
    '''Для створення продуктів у магазині.'''
    
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        Storage.add_to_Storage(self)
    
        
class Storage(Product):
    '''Склад для наявних продуктів.'''
    
    list_products = []
    
    def __init__(self, type, name, price):
        super().__init__(type, name, price)
    
    def add_to_Storage(self, list_products=list_products):
        '''Добавляє створені продукти до складу.'''
        if len(list_products):
            for i in range(len(list_products)):
                if self.type in list(iter(list_products[i])):
                    dict_1 = {}
                    dict_1[self.name] = self.price
                    list_products[i][self.type].append(dict_1)
                    return list_products
            else:    
                dict = {}
                dict[self.type] = []
                dict_depth = dict[self.type]
                dict_1 = {}
                dict_1[self.name] = self.price
                dict_depth.append(dict_1)
                list_products.append(dict)
                
        else:
            dict = {}
            dict[self.type] = []
            dict_depth = dict[self.type]
            dict_1 = {}
            dict_1[self.name] = self.price
            dict_depth.append(dict_1)
            list_products.append(dict)

class Till:
    '''Клас для збереження інформації про заробіток та відомостей про продажію.'''
    
    till = 0
    
    list_for_cheques = [{}]
    list_for_cheque = []
    
    def add_to_list(list_for_cheque=list_for_cheque, list_for_cheques=list_for_cheques):
        '''Добавляє товари під час продажу до відомості про продажі.'''
        import time
        x = len(list_for_cheques)-1
        list_for_cheques[x][time.strftime('%x: %X')] = list_for_cheque

class ProductStore(Till):
    '''Клас для роботи з товаром.'''        
    
    def add(cls, product, amount):
        '''Робить націнку на товар.'''
        return (amount*product.price*1.3)
    
    def set_discount(cls, identifier, percent):
        '''Робить знижку на вказаний товар.'''
        list = Storage.list_products
        for i in range(len(list)):
            if identifier == next(iter(list[i].keys())):
                list_1 = next(iter(list[i].values()))            
                for dict in list_1:
                    del list_1[0]
                    key = next(iter(dict.keys()))
                    value = dict.pop(key)
                    value *= (1 - percent/100)
                    dict[key] = value
                    list_1.append(dict)
                    continue
                else:
                    return list
            list_1 = next(iter(list[i].values()))
            for p in range(len(list_1)):
                if identifier in next(iter(list_1[p].keys())):
                    value = list_1[p].pop(identifier)
                    value *= (1 - percent/100)
                    list_1[p][identifier] = value
            return list
    
    def sell_product(cls, product_name, amount, cost):
        '''Робить продаж товару та фіксує його у відомостях.'''
        list = Storage.list_products
        list_for_cheque = []
        for dict_0 in list: 
            for value in dict_0.values():
                list_for_dict = value
            dictionary = []
            for dict_1 in list_for_dict:
                dictionary.append(dict_1)
            items = []
            for diction in dictionary:
                items.append(diction.items())
            items_new = []
            for item in items:
                items_new += item  
            
            while items_new:
                n = items_new.count(items_new[0])
                key = items_new[0][0]
                value = items_new[0][1]
                if product_name == key and cost == value:
                    if n < amount:
                        raise ValueError('Заданої кількості цього продукту немає в наявності.')
                    else:
                        n = amount
                        while n > 0:
                            list_for_cheque.append((key, value))
                            n -= 1
                        Till.list_for_cheque = list_for_cheque
                        list_for_cheques = Till.list_for_cheques
                        Till.add_to_list(list_for_cheque=list_for_cheque, list_for_cheques=list_for_cheques)
                        Till.till += cost*amount
                        items_new.clear()
                else:
                    items_new.remove(items_new[0])
        
    
        preset_dictionary = {}
        preset_dictionary[product_name] = cost
# =============================================================================
#         for i in range(len(Storage.list_products)):
#             for key in Storage.list_products[i].keys():
#                 for j in range(len(Storage.list_products[i][key])):
#                     for item in Storage.list_products[i][key][j].items():
#                         if item == (product_name, cost):
#                             list_for_cheque.append(Storage.list_products[i][key][j])
#                             del Storage.list_products[i][key][j]
#                             amount -= 1
#                             if amount > 0:
#                                 break
#                         if amount > 0:
#                             break
#                     if amount > 0:
#                         break
#                 if amount > 0:
#                     continue
# =============================================================================
        list_base = []
        for i in range(len(Storage.list_products)):
            for key in Storage.list_products[i].keys():
                list_0 = [dict for dict in Storage.list_products[i][key]]
                list_base += [list_0]
        for list in list_base:
            i = len(list)
            while (i > 0 and amount > 0):
                 if preset_dictionary in list:
                    list.remove({'T-shirt': 200})
                    amount -= 1
                 else:
                    i -= 1 
        for i in range(len(Storage.list_products)):
            for key in Storage.list_products[i].keys():
                 Storage.list_products[i][key] = list_base[0]
                 del list_base[0]
    
        return Till.till
    
    def get_income(cls):
        '''Повертає суму зароблених грошей з продаж.'''
        return Till.till

    def get_cheques(cls):
        '''Повертає відомості по продажам.'''
        return Till.list_for_cheques
    
    def get_all_products(cls):
        '''Показує наявний товар.'''
        return Storage.list_products
    
    def get_product_info(cls, product_name):
        '''Показує інофрмацію по вказаному товару (назва, ціна, кількість на складі).'''
        list = Storage.list_products[:]
        list_for_product = [] 
        for i in range(len(list)): 
            list_n = [value for value in list[i].values()]
            dictionary = [list_n[0][i] for i in range(len(list_n[0]))]
            items_m = [diction.items() for diction in dictionary]
            items = []
            for j in range(len(items_m)):
                item = [item for item in items_m[j]][0]  
                items.append(item)
            while items:
                n = items.count(items[0])
                key = items[0][0]
                if product_name == key:
                    value = items[0][1]
                    ware = (key, value, n)
                    list_for_product.append(ware)
                    while n > 0:
                        items.remove((key, value))
                        n -= 1
                    continue
                else:
                    items.remove(items[0])
        return list_for_product      
                
                
u = Product('Sport', 'T-shirt', 125)        
a = Product('Sport', 'T-shirt', 200)
t = Product('Sport', 'Short', 123)
g = Product('Sport', 'T-shirt', 200)
f = Product('Sport', 'T-shirt', 125)
b = Product('Sport', 'T-shirt', 200)
h = Product('Fruit', 'tomato', 200)
j = Product('Fruit', 'apple', 200)

print(Storage.list_products)

o = ProductStore()

print(o.sell_product('T-shirt', 2, 125))

print(Storage.list_products)

print(o.get_product_info('T-shirt'))

print(o.get_cheques())

