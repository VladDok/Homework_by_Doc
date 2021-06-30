def add_data(data_book, year, count):
    '''Функція для заповнення словника'''
    
    if type(data_book) == dict:
        data_book[year] = count
        return data_book
    else:
        raise TypeError('Data_book might be only type "dict".')

