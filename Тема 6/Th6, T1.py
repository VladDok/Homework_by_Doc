# Make a program that has some sentence (a string) on input and returns a dict 
# containing all unique words as keys and the number of occurrences as values. 

print('Hello considered user. This program use for searching keys words\n
and their amount. You can see example the work this program. Do you\n
want to use this program for your goals or want to look at example.')

while True:
    answer_user = input('1 - want to see example\n2 - want to use in my goals\n\
Your answer: ')

    if answer_user == '1':
        text = '''The prices of several cryptocurrencies, which were soaring high 
in April, have plunged more than 40 per cent in the weeks since Tesla chief 
Elon Musk said the company would no longer accept bitcoin as payment, 
and now investors are pleading with the billionaire to stop tweeting about 
the digital currency.
Earlier this month, Musk jokingly called Dogecoin a “hustle” during 
his appearance on the late-night comedy show SNL. That, along with 
a series of events including China’s crackdown on cryptocurrency transactions 
and mining, crashed the prices of several digital tokens further.
“Do not pay attention to Elon Musk’s comments about anything in crypto 
at least over the longer term,” William Quigley, 
Managing Director of Magnetic, a cryptocurrency investing firm, 
said in a recent interview on CNN Business.
Several investors point to Musk’s tweet as a tipping point in bitcoin’s 
biggest collapse of the year, which was peaking even as late as mid-April 
at close to $65,000.
“Tesla until very recently was going to accept bitcoin as a payment. 
That alone told me he didn’t really understand how to think 
about bitcoin,” Quigley said.'''
    
        list_for_text = text.split('.')
        string = ' '.join(list_for_text)
        list_for_text = string.split(' ')
        list_for_text_new = []
    
        for word in list_for_text:
            list_with_correct_char = [word[i] for i in range(len(word)) 
              if word[i].isalnum() == True or '’' in word[1:len(word)-1] or '-' 
              in word[1:len(word)-1] or '\'' in word[1:len(word)-1]]
            correct_word = ''.join(list_with_correct_char)
            check_on_empty = bool(correct_word)
            if check_on_empty:
                list_for_text_new.append(correct_word)
    
        list_of_words_for_dict = []
        list_of_amount_words = []
    
        for word in list_for_text_new:
            if word not in list_of_words_for_dict:
                list_of_words_for_dict.append(word)
                amount_of_word = list_for_text_new.count(word)
                list_of_amount_words.append(amount_of_word)
    
        main_dict = {}
    
        for i in zip(list_of_words_for_dict, list_of_amount_words):
            main_dict[i[0]] = i[1]
    
        print(main_dict)
        print('\nAnd now what are you doing?')
        continue

    elif answer_user == '2':
        text = input('Write your text: ')
    
        list_for_text = text.split('.')
        string = ' '.join(list_for_text)
        list_for_text = string.split(' ')
        list_for_text_new = []
    
        for word in list_for_text:
            list_with_correct_char = [word[i] for i in range(len(word)) 
              if word[i].isalnum() == True or '’' in word[1:len(word)-1] or '-' 
              in word[1:len(word)-1] or '\'' in word[1:len(word)-1]]
            correct_word = ''.join(list_with_correct_char)
            check_on_empty = bool(correct_word)
            if check_on_empty:
                list_for_text_new.append(correct_word)
    
        list_of_words_for_dict = []
        list_of_amount_words = []
    
        for word in list_for_text_new:
            if word not in list_of_words_for_dict:
                list_of_words_for_dict.append(word)
                amount_of_word = list_for_text_new.count(word)
                list_of_amount_words.append(amount_of_word)
    
        main_dict = {}
    
        for i in zip(list_of_words_for_dict, list_of_amount_words):
            main_dict[i[0]] = i[1]
    
        print(main_dict)
        
        answer_user_after_work =input('You want to finish or return? \
(1 or 0)\n')
        if  answer_user_after_work == '1':
            continue
        else:
            break        
    else:
        print('Change 1 or 2.')
        continue

print('Good day!')
    
        
            
    
    

                
            
