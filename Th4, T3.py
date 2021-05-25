from random import randint

print('Доброго дня шанjвний користувачу!\nДана програма створена з метою перетворення уведеного рядку у 5 комбінацій різних рядків, які висвітляться у стовпчик.\nПриємного користування!')
while True:
    answer = input('Уведіть рядок: ')
    h = 0
    j = 0
    while h < len(answer):
        if answer[h].isdigit() == True:
            j = 1
            h += 1
        else:
            h += 1
    if j == 1:
        print('\nРядок неповинен містити числа!')
        continue
    r = 0
    t = 0
    correct1 = []
    while r < len(answer):
        if answer[r] in correct1:
            t = 1
            r += 1
        else:
            correct1.append(answer[r])
            r += 1
    if t == 1:
        print('\nУ трьох буквинному реченні неповинні повторюватися 2 букви!')
        continue
    else:
        if len(answer) <= 2 :
            print('\nСлово повинно містити більше 2 букв!')
            continue
        else:
            g = 0
            correct = []
            while g < 5:
                s_g = ''
                correct_g = []
                f = 0
                while f < len(answer):
                    i = randint(0, len(answer) - 1)
                    if i in correct_g:
                        continue
                    else:
                        correct_g.append(i)
                        s_g += answer[i]
                        f += 1
                if s_g in correct:
                    continue
                else:
                    correct.append(s_g)
                    print(f'Копія номер {g}:', s_g)
                    g += 1
            break
    

