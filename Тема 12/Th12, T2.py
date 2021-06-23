# =============================================================================
# Library
# 
# Write a class structure that implements a library. Classes:
# 
# 1) Library - name, books = [], authors = []
# 
# 2) Book - name, year, author (author must be an instance of Author class)
# 
# 3) Author - name, country, birthday, books = []
# 
# Library class
# 
# Methods:
# 
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# 
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# 
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# 
# All 3 classes must have a readable __repr__ and __str__ methods.
# 
# Also, the book class should have a class variable which holds the amount of all existing books
# 
# ```
# 
# class Library:
# 
#     pass
# 
#  
# 
# class Book:
# 
#     pass
# 
#  
# 
# class Author:
# 
#     pass
# 
# ```
# =============================================================================

class Author:
    '''Картотека про авторів'''
    
    list_for_authors = []
    
    def __init__(self, name, country, birthday):
        self.name = name 
        self.country = country
        self.birthday = birthday
        self.books = [next(iter(book.keys())) for book in Book.list_books if self.name in next(iter(book.values()))[0]]
        Author.list_for_authors.append(self.name)
    
    def __str__(self):
        return f'{self.name.title()} was born in {self.birthday} in {self.country.title()}.\n\
Author have next books: {[book for book in self.books]}.'
    
    def __repr__(self):
        return f'{self.name.title()} was born in {self.birthday} in {self.country.title()}.\n\
Author have next books: {[book.capitalize() for book in self.books]}'
         

class Book:
    '''Книга'''
    
    list_books = []
    amount = 0
            
    def add_new_book_to_list(name, year, author, list):
        '''Добавляє книги в лист'''
        list.append({name: [author, year]})
        
    def add_book_to_amount(list):
        '''Рахує кількість наявних книг'''
        Book.amount = len(list)
    
    def __init__(self, name, year, author):
        self.name = name.capitalize()
        self.year = year
        self.author = author.title()
        Book.add_new_book_to_list(self.name, self.year, self.author, Book.list_books)
        Book.add_book_to_amount(Book.list_books)
        try:
            if Author.books:
                Author.books.append({self.name:self.year})
        except AttributeError:
            pass
          
    def __str__(self):
        return f'{self.name.title()}, {self.year}. Author: {self.author.title()}.'
    
    def __repr__(self):
        return f'{self.name.title()}, {self.year}. Author: {self.author.title()}.'
         

class Library:
    '''Для імітації бібліотеки.'''
    
    def __init__(self, name):
        self.name = name
        self.books = Book.list_books
        self.authors = Author.list_for_authors
   
    def __str__(self):
        return f'{self.name.title()} have next books: {[next(iter(book.keys())) for book in self.books]},\n\
and information about next authors: {[author.title() for author in self.authors]}.'
    
    def __repr__(self):
        return f'{self.name.title()} have next books: {[next(iter(book.keys())) for book in self.books]},\n\
and information about next authors: {[author.title() for author in self.authors]}.'
        

book1 = Book('Тіні забутих предків', 1912, 'Михайло Коцюбинський')
book2 = Book('Алхімік', 1988, 'Пауло Коельйо')
book3 = Book('Війна і мир', 1867, 'Лєв Толстий')

print(Book.list_books)
print(Book.amount)
print('')

author1 = Author('Михайло Коцюбинський', 'Україна', '17.09.1864')

print(Author.list_for_authors)
print(author1)
print('')

lib1 = Library('Book')

print(lib1)
        

