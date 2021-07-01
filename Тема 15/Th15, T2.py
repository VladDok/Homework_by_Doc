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
    
    def __str__(self):
        return 'Боса з даним id ненайдено.'



def take_id(name, company='Tesla', data_id=exist_id):
    
    if data_id.get(company.title(), False):
        list_id_workers = data_id.get(company.title())
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
    
    def __init__(self, name, company='Tesla'):
        self.name = name.title()
        self.id = take_id(self.name)
        self.company = company.title()
        self._workers = []
        Check_id_of_Boss.add_id(self.id)
        take_worker(self.id, self.name, Boss.__name__)  
        
    
    def workers(self, id_worker, name_worker):
        data_worker = {}
        data_worker[id_worker] = name_worker
        self._workers.append(data_worker)
    
        
class Check_id_of_Boss(Boss):
    
    data_id_boss = []
    
    def add_id(id_boss):
        Check_id_of_Boss.data_id_boss.append(id_boss)


class Worker:
    
    def __init__(self, name, id_boss, company='Tesla',):
        if id_boss in Check_id_of_Boss.data_id_boss:
            self.name = name.title()
            self.id = take_id(self.name)
            self.company = company.title()
            take_worker(self.id, self.name, Worker.__name__)
        else:
            raise NotFoundBoss
            
#Добавити можливість добавляти працівників

