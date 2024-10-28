""" 

Vytvořte simulaci knihovny. Knihovna bude reprezentována seznamem knih. Každá kniha bude reprezentována slovníkem s následujícími klíči:

'title': Název knihy (řetězec).
'author': Autor knihy (řetězec).
'genre': Žánr knihy (řetězec).
'available': Logická hodnota, která udává, zda je kniha dostupná (True) nebo vypůjčená (False).

Nyní vytvořte následující funkce:

    * add_book(book): Přidá knihu do knihovny (seznamu knih), pokud kniha s daným názvem již v knihovně není. Funkce vrátí True, pokud byla kniha úspěšně přidána, a False, pokud kniha již v knihovně existuje.

    * borrow_book(title): Zapůjčí knihu z knihovny. Pokud je kniha dostupná, nastaví available na False a vrátí True. Pokud je kniha již vypůjčená nebo neexistuje, vrátí False.

    * return_book(title): Vrátí knihu do knihovny. Pokud je kniha vypůjčená a existuje v knihovně, nastaví available na True a vrátí True. Pokud kniha neexistuje nebo je již dostupná, vrátí False.

    * get_books_by_genre(genre): Vrátí seznam všech knih v knihovně daného žánru. Seznam bude obsahovat slovníky reprezentující jednotlivé knihy.

    * get_available_books(): Vrátí seznam všech dostupných knih v knihovně. Seznam bude obsahovat slovníky reprezentující jednotlivé knihy.

    * remove_book(title): Odebere knihu z knihovny. Pokud kniha existuje, odstraní ji a vrátí True. Pokud kniha neexistuje, vrátí False. 

"""


library = []


def add_book(book):
    title = book['title']
    for existing_book in library:
        if existing_book['title'] == title:
            return False
    library.append(book)
    return True


def borrow_book(title):
    for book in library:
        if book['title'] == title:
            if book['available']:
                book['available'] = False
                return True
            else:
                return False
    return False


def return_book(title):
    for book in library:
        if book['title'] == title:
            if not book['available']:
                book['available'] = True
                return True
            else:
                return False
    return False


def get_books_by_genre(genre):
    genre_books = []
    for book in library:
        if book['genre'] == genre:
            genre_books.append(book)
    return genre_books


def get_available_books():
    available_books = []
    for book in library:
        if book['available'] == True:
            available_books.append(book)
    return available_books


def remove_book(title):
    for book in library:
        if book['title'] == title:
            library.remove(book)
            return True
    return False


# tímto způsobem pak přidáme knihy
add_book({'title': "Harry Potter and the Philosopher's Stone", 'author': 'J.K. Rowling', 'genre': 'Fantasy', 'available': True})
add_book({'title': 'The Alchemist', 'author': 'Paulo Coelho', 'genre': 'Novel', 'available': True})

# když si teď knihovnu vypíšeme, už v ní budou přidané knihy
print(library)

# následně si jednu knihu vypůjčíme
borrow_book('The Alchemist')

# teď by se měla změnit dostupnost z True na False u knihy, kterou jsme si vypůjčili
print(library)

# hned poté knihu pomocí funkce return_book vrátíme
return_book('The Alchemist')

# a knihu máme opět dostupnou pro další vypůjčení!
print(library)

# tímto způsobem zavoláme funkci, která vypíše knihy zvoleného žánru
print(get_books_by_genre('Novel'))

# vypíšeme všechny dostupné knihy
print(get_available_books())

# pomocí této funkce můžeme knihy odstraňovat
remove_book('The Alchemist')

# po odstranění, už nám zbývá jen jedna kniha
print(library)