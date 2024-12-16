"""
    * Na zpracování máte 45 minut.
    * Celkově je možné získat 40 bodů.
    * Odevzdávejte do odevzdávárny v isu jako jeden .py soubor.


Praktická aplikace:

Vytvořte aplikaci pro správu rezervací hotelových pokojů, kde každý pokoj bude reprezentován jako slovník s následujícími klíči:
 
'room_number': číslo pokoje (řetězec)
'room_type': typ pokoje (řetězec, např. "jednolůžkový", "dvoulůžkový")
'price': cena za noc (celé číslo)
'available': stav pokoje (True/False)
 
Napište následující funkce:

1. add_room(room): Přidá nový pokoj do seznamu, pokud neexistuje pokoj se stejným číslem. Pokud byl přidán, vrátí True. Jinak vrátí False. (5 b.)
2. book_room(room_number): Pokud je pokoj dostupný, označí ho jako obsazený (available = False) a vrátí True. Pokud je již obsazen, vrátí False. (6 b.)
3. get_available_rooms(): Vrátí seznam všech dostupných pokojů. (6 b.)
4. find_room_by_type(room_type): Vyhledá pokoje podle typu (např. "dvoulůžkový"). Vrátí seznam odpovídajících pokojů. (6 b.)
5. room_price(limit): Vrátí všechny pokoje, jejichž cena za noc je menší nebo rovna dané hranici. (6 b.)
6. remove_room(room_number): Odstraní pokoj se zadaným číslem. Pokud existuje, vrátí True, jinak vrátí False. (6 b.)

"""


