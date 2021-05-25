from random import randrange
from math import log10
from math import sqrt
from time import sleep

print('Доброго дня шановний учасник математичної вікторини!')

ask_1 = input('Ти справді бажаєш спробувати свої сили?\n 1 - так;\n 2 - ні.\nТвоя відповідь: ')
if ask_1 == '1':
    print('\nБачу в твоїх очах відвагу!')  
    while True:
        ask_2 = input('Обери свій рівень складності:\n 1 - easy;\n 2 - medium;\n 3 - hard;\nТвоя відповідь: ')
        if ask_2 == '1':
            a = randrange(-100, 100)
            b = randrange(-100, 100)
            equal = a + b
            if a > 0 and b > 0 or a < 0 and b > 0:
                print(f'\nx = {a} + {b}')
            else:
                print(f'\nx = {a} - {-b}')
            while True:
                x_1 = int(input('Чому рівний x?\n'))
                if x_1 == equal:
                    sleep(3)
                    print('\nМолодець. Хммм...')
                    break
                else:
                    sleep(3)
                    print('\nНевірно. Спробуй ще!')
                    continue
            ask_3 = input('Можливо ти себе недооцінюєш і спробуєш на рівень вище?\n1 - так;\n2 - ні.\n')
            if ask_3 == '1':
                continue
            else:
                break
                
        elif ask_2 == '2':
            while True:
                while True:
                    a = randrange(-5, 5)
                    x_1 = randrange(-15, 15)
                    x_2 = randrange(-15, 15)
                    b = a*(x_1 + x_2)
                    c = a*x_1*x_2
                    if a == 0 and b == 0:
                        continue
                    else:
                        break
                if (b**2 - 4*a*c) < 0:
                    continue
                else:
                    break
            x_1 = str(int((-b + sqrt(b**2 - 4*a*c))/2*a))
            x_2 = str(int((-b - sqrt(b**2 - 4*a*c))/2*a))
            if b > 0 and c < 0:
                print(f'\n{a}*x**2 + {b}*x - {-c} = 0') 
            elif b < 0 and c > 0:
                print(f'\n{a}*x**2 - {-b}*x + {c} = 0')
            elif b < 0 and c < 0:
                print(f'\n{a}*x**2 - {-b}*x - {-c} = 0')
            else:
                print(f'\n{a}*x**2 + {b}*x + {c} = 0')
            solve = sorted([x_1, x_2])
            while True:
                x_3 = input('Чому рівний x1 та x2?\nФормат відповіді: x1,x2\n').split(',')
                x_3.sort()
                if x_3 == solve:
                    sleep(3)
                    print('\nВидно, що ти спеціаліст. Браво!')
                    break
                else:
                    sleep(3)
                    print('\nНевірно!\nСпробуй ще раз.')
                    continue
            ask_3 = input('Можливо ти себе недооцінюєш і спробуєш на рівень вище?\n1 - так;\n2 - ні.\n')
            if ask_3 == '1':
                continue
            else:
                break
        else:
            a = randrange(-100, 100, 10)
            b = randrange(-100, 100, 10)
            c = randrange(-10, 10)
            d = randrange(-10, 10)
            e = 10
            solve = round((log10(e)/log10(a*b))/(c+d), 2)
            if b > 0:
                print(f'\n{a}**({c}*x) + {b}**({d}*x) = {e}')
            else:
                print(f'\n{a}**({c}*x) - {-b}**({d}*x) = {e}')
            while True:
                x_4 = input('Чому рівний х? (відповідь заокругліть до двух знаків після коми)\n')
                if x_4 == str(solve):
                    sleep(3)
                    print('\nМаестро! Філігранна робота. Тобі усе під силу.')
                    break
                else:
                    sleep(3)
                    print('\nУпс... Помилка.\nСпробуй ще.')
                    continue
            ask_4 = input('\nМожливо хочеш спробувати ще?(1 або 0)\n')
            if ask_4 == '1':
                continue
            else: 
                break

else:
    print('\nДо наступних зустрічей!')
    
print('\nДо наступних зустрічей!')
            
                
            
            
            
             
        









