# The name check.

# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
# The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
# if your input is “Anton” and the stored name is “anton”, it should return True.

# My solution

base_name = []

print('Доброго дня! Уведіть Ваше ім\'я для збереження у нашій базі даних та подальшого звірення з нею.')

def f():   
    ask = input('Хочете зберегти нове ім\'я?\n1 - так\n0 - ні\n')
    if ask == '1':
        print(g())
    elif ask == '0':
        print('Гарного Вам дня!')
    else:
        print('\nВиберіть одну із вказаних вище відповідей.')
        f()

def ans():
    while True:
        name_1 = input('Уведіть ваше ім\'я для звірення з базою: ')
        if name_1.lower() == f'{name}':
            print('Так, дане ім\'я збережене у базі.')
            break
        elif name_1.lower() != 'f{name}':
            print('Даного імені нема в базі даних. Спробуйте ще раз')
            continue
    f()

def g():
    global name
    name = input('У ведіть ваше ім\'я: ')
    base_name.append(name.lower())
    print(f'{name} успішно збережено. Дякую!')       
    ans()

g()

