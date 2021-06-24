class CustomException(Exception):
    '''Клас генератор помилок із подальшим записом у файл'''
    
    def __init__(self, msg):
        self.text = msg
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(str(self.text))
        

a = input('Уведіть число: ')

for i in range(len(a)):
    try:
        if a[i].isalpha():
            raise CustomException('Неможна використовувати літери.')
    except CustomException as ex:
        error = CustomException(ex)
else:
    print('Інформація збережена.')

