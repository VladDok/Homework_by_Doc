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

