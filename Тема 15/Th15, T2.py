# =============================================================================
# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# 
# Worker has a property 'boss', and its value must be an instance of Boss.
# 
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
# 
# You can refactor the existing code.
# 
# ```
# 
# id_ - is just a random unique integer
# 
#  
# 
# class Boss:
# 
#     def __init__(self, id_: int, name: str, company: str):
# 
#         self.id = id_
# 
#         self.name = name
# 
#         self.company = company
# 
#         self.workers = []
# 
#  
# 
# class Worker:
# 
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
# 
#         self.id = id_
# 
#         self.name = name
# 
#         self.company = company
# 
#         self.boss = boss
# 
# ```
# =============================================================================

from random import randint

exist_id = {}
exist_worker = {}

class NotFoundBoss(Exception):
    """Специфічна помилка для помилки пошуку id."""
    
    def __str__(self):
        return 'Боса з даним id ненайдено.'
    
class NotFoundPlace(Exception):
    """Помилка при відсутності нових вакансій."""

    def __str__(self):
        return 'Вільних вакансій немає.'

def take_id(name, company='Tesla', data_id=exist_id):
    """Створення унікального id для кожного працівника."""
    
    if data_id.get(company.title(), False):
        list_id_workers = data_id.get(company.title())
        lenght_of_list = len(list_id_workers)
        
        if lenght_of_list == 100:
            raise NotFoundPlace
        
        while True:
            ind = 0
            new_id = randint(1, 100)
            for dict_id in list_id_workers:
                if dict_id.get(new_id, False):
                    ind = 1
                    break
            if ind == 1:
                continue
            else:
                break
        
        new_data = {}
        new_data[new_id] = name
        list_id_workers.append(new_data)
        data_id[company] = list_id_workers
    
    else:
        data_id[company] = []
        
        new_id = randint(1, 100)
        new_data = {}
        new_data[new_id] = name
        
        list_id = data_id[company]
        list_id.append(new_data)
        data_id[company] = list_id          

    return new_id

def take_worker(id, name, status, company='Tesla', data_workers=exist_worker):
    """Добавлення усіх працівників у загальний реєстр exist_worker."""
    if data_workers.get(company.title(), False):
        list_workers = data_workers.get(company.title())
        new_worker = {}
        new_worker[status] = [id, name]
        list_workers.append(new_worker)
        data_workers[company.title()] = list_workers
    
    else:
        new_worker = {}
        new_worker[status] = [id, name]
        list_workers = [new_worker]
        data_workers[company.title()] = list_workers
    
    return ''


class Boss:
    
    list_Boss_Workers = []
    
    def __init__(self, name, company='Tesla'):
        self.name = name.title()
        self.id = take_id(self.name)
        self.company = company.title()
        take_worker(self.id, self.name, Boss.__name__)
        boss = {}
        boss[self.id] = []
        Boss.list_Boss_Workers.append(boss)
            
    
    def workers(self, id_worker, name_worker):
        data_worker = {}
        data_worker[id_worker] = name_worker
        self._workers.append(data_worker)
    
    def __name__(self):
        return self


class Worker:

    def __init__(self, name, id_boss, company='Tesla',):
        ind = 0
        for boss in Boss.list_Boss_Workers:
            for key in boss.keys(): 
                if id_boss == key:
                    self.name = name.title()
                    self.id = take_id(self.name)
                    self.company = company.title()
                    take_worker(self.id, self.name, Worker.__name__)
                    for diction in Boss.list_Boss_Workers:
                        list_workers = diction.get(id_boss, False)
                        if type(list_workers) == list:
                            inf_for_worker = {}
                            inf_for_worker[self.id] = self.name
                            list_workers.append(inf_for_worker)
                            new_diction = {}
                            new_diction[id_boss] = list_workers
                    ind = 1
                    break
            if ind == 1:
                break
                                        
        else:
            print('Компанія неможе існувати без боса. Створіть його, а потім \
наймайте працівників.')
            raise NotFoundBoss

 
# Наймаємо людину, яка буде Босом
john = Boss('john')

# Дістаємо його id
id_boss = [id for id in Boss.list_Boss_Workers[0].keys()][0]

# Наймаємо працівника
rachell = Worker('rachell', id_boss)

# Перевіряємо його наявність в листі
print(Boss.list_Boss_Workers)

print(exist_id) # Список працівників та їх id (специфічний список для перевірки наявних id)
print(exist_worker) # Список усіх працівників та їх статус

