base_tel = []

def a():
    global answer
    answer = input('Ви хочете зареєструвати свій телефон у нашій базі? \n')

def f():
    while answer.lower() == 'yes': 
        ind = 0
        tel = input('Уведіть свій номер телефону: ')
        
        if len(tel) == 10: pass 
        else:
            print('Не використовуйте більше або менше 10 чисел.\n')
            continue
        
        i = 0
        while i < len(tel):
            if tel[i].isdigit():
                i += 1
                continue
            else:
                print('Використовуйте тільки числа при написанні номера телефона.')
                ind = 1
            if ind == 1:
                continue
        base_tel.append(tel)
        print('Ваш телефон внесений у базу. Дякую за співпрацю!')
        break
    else:
        if answer.lower() == 'no':
            print('Гарного Вам дня!')
        else:
            print('Напишіть або yes, або no.')
        
a()

if answer.lower() == 'yes':
    f()
elif answer.lower() == 'no':
    print('Гарного Вам дня!')
else:
    print('\nУВАГА!\n' * 3 + '\nУведіть або yes або no.')
    a()    
           
     
     
    