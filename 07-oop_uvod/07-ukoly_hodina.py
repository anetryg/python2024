#Úkol 1
""" Vytvoř třídu Book s atributy title (název knihy), author (autor knihy) a is_available (informace o dostupnosti knihy - True, pokud je k dispozici, False, pokud je vypůjčená). Přidej metodu borrow_book(), která změní stav dostupnosti knihy na False, pokud je k dispozici. """

class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available
        
    def __str__(self):
        return f"Kniha {self.title} !!"
        
    def borrow_book(self):
        if self.is_available == True:
            self.is_available = False
            print("Knihu máte zapůjčenou")
        else:
            print("Kniha není dostupná")
            
book1 = Book("Hobbit", "Tolkien", True)

book1.borrow_book()
book1.borrow_book()




#Úkol 2
""" Navrhněte třídu LibraryMember s atributy name (jméno člena knihovny) a borrowed_books (seznam knih, které člen vypůjčil). Přidej metodu borrow_book(book), která přidá vypůjčenou knihu do seznamu borrowed_books. """

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(book.title)
        
clen1 = LibraryMember("Šimon")
clen1.borrow_book(book1)


#Úkol 3
""" Vytvoř třídu Account, která bude reprezentovat bankovní účet. Třída by měla mít atributy account_number (číslo účtu), balance (stav účtu) a owner (vlastník účtu). Přidej metodu deposit(amount), která zvýší stav účtu o zadanou částku. """

class Account: 
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        
""" ucet1 = Account(123164, 0, "Aneta")
ucet1.deposit(123)
ucet1.deposit(100) """


#Úkol 4
""" Navrhněte třídu Bank s atributem accounts (seznam bankovních účtů). Přidej metodu create_account(owner, initial_balance), která vytvoří nový bankovní účet a přidá ho do seznamu accounts. """

class Bank:
    def __init__(self, accounts):
        self.accounts=accounts
    
    def create_account(self, owner, initial_balance):
        self.accounts.append(Account(123, initial_balance, owner))
        print(owner,initial_balance)
        
""" banka1=Bank([])
banka1.create_account("Podborská",500) """

    


    
    