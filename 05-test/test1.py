"""
    * Na zpracování máte 60 minut.
    * Celkově je možné získat 40 bodů.
    * Odevzdávejte do odevzdávárny v isu jako jeden .py soubor.


Teoretické otázky. Odpověď vepište rovnou do komentáře zde do souboru. (5 b.)

* Jakým indexem začíná číslování položek v listu? 
* Vysvětli datový typ tuple.
* Jaký je rozdíl mezi "for" cyklem a "while" cyklem?
* Jaký je rozdíl mezi "print" a "return" ve funkci?
* Co znamená ve funkci parametr *args?


Praktická aplikace:

Vytvořte aplikaci pro rezervaci letenek, která bude reprezentována seznamem ve kterém bude každý let reprezentován jako slovník s následujícími klíči:

'flight_number': číslo letu (řetězec)
'departure': místo odletu (řetězec)
'destination': místo příletu (řetězec)
'available_seats': počet volných sedadel (celé číslo)
'price': cena letu (celé číslo)


Napište následující funkce:

* add_flight(flight): Pokud let s takovým číslem letu neexistuje, přidá nový let do seznamu a vrátí True. Pokud let s takovým číslem letu již existuje, pak ho znovu nepřidá a vrátí False. (5 b.)
* book_flight(flight_number, num_seats): Rezervuje zadaný počet sedadel na letu. Pokud jsou dostupná, aktualizuje počet volných sedadel a vrátí True. Pokud není dostatečný počet volných sedadel, vrátí False. (6 b.) 
* get_available_flights(): Vrátí seznam všech letů s dostupnými sedadly. (6 b.)
* find_flights(departure, destination): Vrátí True nebo False na základě toho, jestli existuje daný let na základě odletového a příletového místa. (6 b.)
* flight_price(price): Vrátí všechny lety, které mají cenu pod zadanou hranici. (6 b.)
* remove_flight(flight_number): Odstraní daný let. Pokud takový let existuje, odstraní ho a vrátí True, pokud neexistuje, vrátí False. (6 b.)

"""