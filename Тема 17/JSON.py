# =============================================================================
# Extend Phonebook application
# 
# Functionality of Phonebook application:
# 
# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
#  
# 
# The first argument to the application should be the name 
# of the phonebook. Application should load JSON data, if it is 
# present in the folder with application, else raise an error. 
# After the user exits, all data should be saved to loaded JSON.
# =============================================================================

from cryptography.fernet import Fernet
import json
import os
import sys
import stat

try:        
    def find_fold():
        """Функція для пошуку файлу з телефонною книгою та базою користувачів."""
        name_users = os.getlogin()
        string = 'C:\\' +  f'Users\{name_users}'
        if 'books' in os.listdir(string) and 'data.json' in os.listdir(string + '\\books'):
            with open(string + '\\books\\data.json') as data:
                books = json.load(data)
            
            for dictionary in books:
                if dictionary.keys() not in os.listdir(string + '\\books'):
                    books.remove(dictionary)
                    continue
    
            with open('data.json', 'w') as data:
                json.dump(books, data)
            
            change()
        else:
            print('''\nВітаємо! Для використання контактної книги необхідно
зареєструватися та створити Вашу телефонну книгу.''')
            register()
    
    def change():
        print('Доброго дня!')
        while True:
            print('''Оберіть одну із наступних дій: 
        1 - Зареєструвати нову книгу;
        2 - Пройти ідентифікацію.''')
            answer_user = input('Відповідь: ')
            if answer_user == '1':
                register()
            elif answer_user == '2':
                identificate()
            else:
                print('\nОберіть тільки з двох пропонованих відповідей.\n')
                continue
    
    def register():
        """Для реєстрації користувача та створення його телефонної книги."""
        global name_book
        print('''\nДля реєстрації заповніть наступні поля.''')
        while True:
            login_user = input('Уведіть Ваш логін: ')
            if len(login_user) < 6:
                print('Логін повинен містити більше 6 символів.')
                continue
            else:
                break
        ind_1 = 0
        ind_2 = 0
        while True:
            password_user = input('Уведіть Ваш пароль. Обов\'язково, щоб була одна велика \
літера та 2 числа: ')
            for litera in password_user:
                if litera.isupper(): 
                    ind_1 += 1
                if litera.isdigit(): 
                    ind_2 += 1
            if ind_1 > 0 and ind_2 > 1:
                break
            else:
                print('Даний пароль не є достатньо захищеним. Спробуйте використати \
нашу рекомендацію.')
            continue 
        
        while True:
            name_book = input('Назвіть Вашу телефонну книгу: ')
            if f'{name_book}.json' in os.listdir():
                print('Книга з даним іменем існує! Спробуйте назвати інакше.')
                continue
            elif not name_book:
                print('Назва книги неможе бути пустою.')
                continue
            else:
                break
        data_reg = {hash(name_book):[hash(login_user), hash(password_user)]}
        name_users = os.getlogin()
        string = 'C:\\' +  f'Users\{name_users}'
        
        try:
            os.mkdir(string + '\\books')
        except FileExistsError:
            pass
        os.chdir(string + '\\books')
        with open(f'{name_book}.json', 'w') as book:
            phone_book = []
            json.dump(phone_book, book)
        if 'data.json' not in os.listdir():
            with open('data.json', 'w') as data_file:
                data = []
                data.append(data_reg)
                json.dump(data, data_file)
        else:    
            with open('data.json') as data_file:
                data = json.loads(data_file.read())
                data.append(data_reg)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file)
        encrypt_before_register(name_book)
        call_book(name_book)
    
    def identificate():
        """Для ідентифікації користувача в базі та надання доступу до тел. книги."""
        global name_book
        name_users = os.getlogin()
        string = 'C:\\' +  f'Users\{name_users}'
        os.chdir(string)
        list_for_check1 = os.listdir()
        if 'books' not in list_for_check1:
            print('Ви на даний момент не є зареєстрованими в мережі.\
Спробуйте зареєструватися.')
            register()        
        os.chdir(string + '\\books')
        list_for_check2 = os.listdir()
        if bool(list_for_check2):
            amount_input = 0
            while True:
                ind = 0
                name_book = input('Будь-ласка уведіть назву Вашої книги: ')
                if os.path.isfile(f'{name_book}.json'):
                    with open('data.json') as data_file:
                        data = json.loads(data_file.read())
                    for i in range(len(data)):
                        if str(hash(name_book)) in data[i].keys():
                            loc = i
                            ind = 1
                    if ind == 1:
                            break
                else:
                    print('\nЗаписника з даним іменем неіснує. Спробуйте увести \
ім\'я книги ще раз.')
                    if amount_input == 3:
                        print('Спробуйте згадати та зайти пізніше.')
                        sys.exit()
                    else:
                        amount_input += 1
                        continue
            
            amount_input = 0
            while True:
                login = input('Уведіть Ваш логін: ')
                password = input('Уведіть Ваш пароль: ')
                with open('data.json') as data_file:
                    data = json.loads(data_file.read())
                    login_user = list(data[loc].values())[0][0]
                    password_user = list(data[loc].values())[0][1] 
                    if hash(login) == login_user and hash(password) == password_user:
                        print(f'''Вітаємо шановний користувачу. Телефонна книга 
"{name_book}" успішно приєднана і готова до використання.''')
                        check_on_written(name_book)
                        decrypt(name_book)
                        call_book(name_book)
                    else:
                        if amount_input == 3:
                            print('Спробуйте зайти пізніше.')
                            sys.exit()
                        else:
                            print('\nНевірний логін чи пароль. Спробуйте ще.')
                            amount_input +=1
                            continue
        else:
            print('\nНа даний момент ніяких книг неіснує. Спробуйте зареєструватися.')
            register()
    
    def encrypt_before_register(name_book):
        key = Fernet.generate_key()
        with open(f'{name_book}.key', 'wb') as filekey:
            filekey.write(key)
            
    def encrypt_after_register(name_book):
        with open(f'{name_book}.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        
        with open(f'{name_book}.json', 'rb') as file:
            original = file.read()
            encrypted = fernet.encrypt(original)
        
        with open(f'{name_book}.json', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    
    def decrypt(name_book):
        with open(f'{name_book}.key', 'rb') as filekey:
            key = filekey.read()
        
        fernet = Fernet(key)
    
        with open(f'{name_book}.json', 'rb') as enc_file:
            encrypted = enc_file.read()
    
        decrypted = fernet.decrypt(encrypted)
        with open(f'{name_book}.json', 'wb') as dec_file:
            dec_file.write(decrypted)
    
    def call_book(name_book):
        """Для визначення функціоналу."""
        while True:
            print('''\nОберіть одну із нижче вказаних функцій для продовження роботи.
                  1 - Переглянути всі контакти
                  2 - Додати нові записи;
                  3 - Шукати по імені;
                  4 - Шукати за прізвищем;
                  5 - Шукати за повним ім’ям;
                  6 - Пошук за номером телефону;
                  7 - Пошук за містом;
                  8 - Видалити контакт за повним ім'ям; 
                  9 - Видалити запис для вказаного телефонного номеру;
                  10 - Оновити запис для вказаного повного імені;
                  11 - Оновити запис для вказаного телефонного номера;
                  12 - Вихід з програми.''')
            answer_user = input('Відповідь: ')
            if answer_user == '1':
                print_book(name_book)
            elif answer_user == '2':
                add_notes(name_book)
            elif answer_user == '3':
                find_name(name_book)
            elif answer_user == '4':
                find_surname(name_book)
            elif answer_user == '5':
                find_full_name(name_book)
            elif answer_user == '6':
                find_number_phone(name_book)
            elif answer_user == '7':
                find_city(name_book)
            elif answer_user == '8':
                delete_contact_full_name(name_book)
            elif answer_user == '9':
                delete_contact_phone_number(name_book)
            elif answer_user == '10':
                update_contact_full_name(name_book)
            elif answer_user == '11':
                update_contact_phone_number(name_book)
            elif answer_user == '12':
                exit_book(name_book)
            else:
                print('Обрати можна тільки з перерахованих можливостей.')
                continue
            
    def print_book(name_book):
        with open(f'{name_book}.json') as book:
            data = json.load(book)
            print(data)
    
    def check_on_written(name_book):
        """Функція призначена перевіряти файли на можливість заповнення інформацією."""
        if os.access(f'{name_book}.json', os.W_OK): pass
        else:
            print('\nУ властивостях даного файлу поставлений режим тільки для читання.\n\
\nДаний файл можна знайти в даній директорії:', os.getcwd())
            while True:
                answer = input('Ви хочете змінити режим читання? (1/0)\n')
                if answer == '1':
                    os.chmod('myfile.txt', stat.S_IWRITE)
                    break           
                elif answer == '0':
                    print('\nЯк зміните режим обробки файла, тоді зможете використати дану програму.')
                    break
                else:
                    print('Вибери тільки одну з вказаних відповідей.')
                    continue
    
    def add_data(name, surname, number_phone, city):
        """Для отримання від користувача інофрмації про новий контакт"""
        data = {}
        data['Ім\'я'] = name
        data['Прізвище'] = surname
        data['Номер телефону'] = number_phone
        data['Місто проживання'] = city
        return data
         
    def add_notes(name_book):
        """Функція для створення нового контакту."""
        print('Заповніть нижче вказані поля.')
        name = input('Уведіть ім\'я: ').capitalize()
        surname = input('Уведіть прізвище: ').capitalize()
        while True:
            number_phone = input('Уведіть номер телефону: ')
            if number_phone.isdigit() == False:
                print('Не використовуй при написанні телефону літери.')
                continue
            else:
                break
        while True:
            city = input('Уведіть місто проживання: ').capitalize()
            if city.isalpha() == False:
                print('Невикористовуй при написанні міста числа.')
                continue
            else:
                break
        with open(f'{name_book}.json') as book:
            list_book = json.loads(book.read())
        with open(f'{name_book}.json', 'w') as book:
            data = add_data(name, surname, number_phone, city)
            list_book.append(data)
            json.dump(list_book, book)
        succesfull(name_book)
        
    def present_contact(list_book):
        """Показ усіх знайдених контактів."""
        if not list_book:
            print('\nДанного контакту не знайдено.\n')
        else:
            for i in range(len(list_book)):
                print(list_book[i])
    
    def find(name_book, arg):
        """Функція для пошуку за аргументом."""
        answer_user = (input(f'Укажіть {arg}: ')).capitalize()
        list_book = []
        with open(f'{name_book}.json') as book:
            data = json.load(book)
            for i in range(len(data)):
                if answer_user in (data[i])[arg.capitalize()]:
                    contact = data[i]
                    list_book.append(contact)
        return list_book
        
    def find_name(name_book):
        """Функція для пошуку за іменем."""
        arg = 'ім\'я'
        list_book = find(name_book, arg)
        present_contact(list_book)
        call_book(name_book) 
            
    def find_surname(name_book):
        """Функція для пошуку за прізвищем."""
        arg = 'прізвище'
        list_book = find(name_book, arg)
        present_contact(list_book)
        call_book(name_book) 
            
    def find_full_name(name_book):
        """Функція для пошуку за повним іменем."""
        arg_1 = 'ім\'я'
        arg_2 = 'прізвище'
        list_book1 = find(name_book, arg=arg_1)
        list_book2 = find(name_book, arg=arg_2)
        if list_book1 and list_book2:
            for i in range(len(list_book1)):
                for p in range(len(list_book2)):
                    if list_book2[p] == list_book1[i]:
                        del list_book2[p]
                        continue
            list_book = list_book1 + list_book2
        else:
            list_book = []
        present_contact(list_book)
        call_book(name_book) 
            
    def find_number_phone(name_book):
        """Функція для пошуку за номером телефону."""
        arg = 'номер телефону'
        list_book = find(name_book, arg)
        present_contact(list_book)
        call_book(name_book) 
        
    def find_city(name_book):
        """Функція для пошуку за місцем проживання."""
        arg = 'місто проживання'
        list_book = find(name_book, arg)
        present_contact(list_book)
        call_book(name_book) 
        
    def delete_contact_full_name(name_book):
        """Функція для видалення контакту."""
        arg_1 = 'ім\'я'
        arg_2 = 'прізвище'
        list_book1 = find(name_book, arg=arg_1)
        list_book2 = find(name_book, arg=arg_2)
        if list_book1 and list_book2:
            for i in range(len(list_book1)):
                for p in range(len(list_book2)):
                    if list_book2[p] == list_book1[i]:
                        del list_book2[p]
                        continue
            list_book = list_book1 + list_book2
            if len(list_book) == 1:
                answer = 0
            elif len(list_book) != 1: 
                print(list_book)
                answer = int(input('Оберіть з даних контактів один.\
Рахунок починається зліва направо 1 і ...: '))
                with open(f'{name_book}.json') as book:
                    data = json.load(book)
                with open(f'{name_book}.json', 'w') as book:
                    data.remove(list_book[answer])
                    json.dump(data, book)
        else:
            list_book = []
            present_contact(list_book)  
        call_book(name_book) 
            
    def delete_contact_phone_number(name_book):
        """Для видалення контакту за номером телефону."""
        arg = 'номер телефону'
        list_book = find(name_book, arg = arg)
        if list_book:
            with open(f'{name_book}.json') as book:
                data = json.load(book)
            with open(f'{name_book}.json', 'w') as book:
                data.remove(list_book[0])
                if not data:
                    data = []
                else: pass
                json.dump(data, book)
        else:
            print('Контакту з таким номером неіснує.')
        call_book(name_book) 
    
    def update_contact_full_name(name_book):
        """Функція для коригування інформації в контакті."""
        arg_1 = 'ім\'я'
        arg_2 = 'прізвище'
        list_book1 = find(name_book, arg=arg_1)
        list_book2 = find(name_book, arg=arg_2)
        if list_book1 and list_book2:
            for i in range(len(list_book1)):
                for p in range(len(list_book2)):
                    if list_book2[p] == list_book1[i]:
                        del list_book2[p]
                        continue
            list_book = list_book1 + list_book2
        else:
            list_book = []
            present_contact(list_book)  
        if len(list_book) == 1:
            answer = 0
        elif len(list_book) != 1: 
            print(list_book)
            answer = int(input('Оберіть з даних контактів один.\
Рахунок починається зліва направо 1 і ...: '))
        with open(f'{name_book}.json') as book:
            data = json.load(book)
        with open(f'{name_book}.json', 'w') as book:
            data.remove(list_book[answer])
            json.dump(data, book)
        add_notes(name_book)
        succesfull(name_book)
        call_book(name_book)
        
    def update_contact_phone_number(name_book):
        """Функція для оновлення запису по вказаному номеру телефона."""
        delete_contact_phone_number(name_book)
        add_notes(name_book)
        succesfull(name_book)
        call_book(name_book)
        
    def exit_book(name_book):
        """Функція для виходу з книги."""
        encrypt_after_register(name_book)
        os.remove('file_for_name.txt')
        print('Гарного тобі дня!')
        sys.exit()
    
    def succesfull(name_book):
        """Функція для оголошення про успішне збереження інформації."""
        print('\nІнформація збережена успішно!\n')
        call_book(name_book)        

    find_fold()
except:
    print('Трапилася помилка. Спробуйте перезапустити програму.')
    
finally:
    encrypt_after_register(name_book)
        
