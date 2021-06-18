class CustomException(Exception):
    '''Клас генератор помилок із подальшим записом у файл'''
    
    def __init__(self, msg):
        self.msg = msg 
        with open('logs.txt', 'w') as log:
            log.write(self.msg)
        
            


    
    