# Write a script that creates a new output file called myfile.txt 
# and writes the string "Hello file world!" in it. Then write another 
# script that opens myfile.txt, and reads and prints its contents. 
# Run your two scripts from the system command line. 
 
# Does the new file show up in the directory where you ran your scripts? 

# What if you add a different directory path to the filename passed to open?

# Note: file write methods do not add newline characters to your strings; 
# add an explicit ‘\n’ at the end of the string if you want to fully terminate 
# the line in the file.

import os
import stat

while True:
    try:
        with open('myfile.txt', 'w') as file:
            file.write('Hello file world!\n')
        break
    except PermissionError:
        print('\nУ властивостях даного файлу поставлений режим тільки для читання.\n\
    \nДаний файл можна знайти в даній директорії:', os.getcwd())
        while True:
            answer = input('Ви хочете змінити режим читання? (1/0)\n')
            if answer == '1':
                os.chmod('myfile.txt', stat.S_IWRITE)
                ind = 1
                break           
            elif answer == '0':
                print('\nЯк зміните режим обробки файла, тоді зможете використати дану програму.')
                ind = 0
                break
            else:
                print('Вибери тільки одну з вказаних відповідей.')
                continue
        if ind == 1:
            continue
        else:
            break

