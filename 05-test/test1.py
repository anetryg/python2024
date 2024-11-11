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

flights = []

def add_flight(flight):
    for existing_flight in flights:
        if existing_flight['flight_number'] == flight['flight_number']:
            return False
    flights.append(flight)
    return True


def book_flight(flight_number, num_seats):
    for flight in flights:
        if flight['flight_number'] == flight_number:
            if flight['available_seats'] >= num_seats:
                flight['available_seats'] -= num_seats
                return True
            else:
                return False
    return False


def get_available_flights():
    available_flights = []
    for flight in flights:
        if flight['available_seats'] > 0:
            available_flights.append(flight)
    return available_flights


def find_flights(departure, destination):
    for flight in flights:
        if flight['departure'] == departure and flight['destination'] == destination:
            return True
    return False


def flight_price(price):
    affordable_flights = []
    for flight in flights:
        if flight['price'] < price:
            affordable_flights.append(flight)
    return affordable_flights


def remove_flight(flight_number):
    for flight in flights:
        if flight['flight_number'] == flight_number:
            flights.remove(flight)
            return True
    return False


# Příklad použití:

flight1 = {'flight_number': 'ABC123', 'departure': 'Prague', 'destination': 'Paris', 'available_seats': 100, 'price': 200}
flight2 = {'flight_number': 'DEF456', 'departure': 'Berlin', 'destination': 'London', 'available_seats': 50, 'price': 150}

add_flight(flight1)
add_flight(flight2)

print(get_available_flights())  # Vypíše všechny lety s dostupnými sedadly

book_flight('ABC123', 30)
book_flight('DEF456', 60)

print(get_available_flights())  # Vypíše lety s dostupnými sedadly po rezervacích

print(find_flights('Prague', 'Paris'))  # True, let existuje
print(find_flights('Prague', 'Berlin'))  # False, let neexistuje

print(flight_price(180))  # Vypíše lety s cenou pod 180

remove_flight('ABC123')
print(get_available_flights())  # Vypíše lety po odstranění letu s číslem 'ABC123'
