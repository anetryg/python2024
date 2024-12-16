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
