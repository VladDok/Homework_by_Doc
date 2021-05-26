# The Guessing Game.

# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
# The result should be sent back to the user via a print statement.

# My solution

from random import randint
from random import randrange

print('Привіт!\nТи відкрив гру \'Угадай число\'.\nБудь ласка, намагайся вгадати число від 1 до 100\nПісля кожної твоєї невдалої спроби число може pvsybnbcz у межах 1, або взагалі незмінитися.')

while True:
    number = randint(1, 100)
    while True:
        try:
            answer = int(input('Як ти думаєш, яке число загадав Рандомайзер?\nТвоя відповідь: '))
        except ValueError:
            print('\nНеможна використовувати букви. Уводь цілі числа.')
            continue   
        if answer < number:
            print('\nТвоє число менше, ніж загадане Рандомайзером.')
            add = randrange(-1, 1)
            number += add
            if number <= 0:
                number += 1
                continue
            else:
                continue  
        elif answer > number:
            print('\nТвоє число більше, ніж загадане Рандомайзером.')
            add = randrange(-1, 1)
            number += add
            if number <= 0:
                number += 1
                continue
            else:
                continue
        else:
            print('\nУрааааа\nТи вгадав. Вітаю!\nМожливо хочеш повторити гру?(yes or no)')
            break
    answer_1 = input('Твоя відповідь: ')
    if answer_1.lower() == 'yes':
        print('Ну що ж, почнімо нову гру!!!')
        continue
    elif answer_1.lower() == 'no':
        print('До нових зустрічей!')
        break

        
                
        
