"""
    * Na zpracování máte 60 minut.
    * Celkově je možné získat 40 bodů.
    * Odevzdávejte do odevzdávárny v isu jako jeden .py soubor.
    

Vaším úkolem bude vytvořit program pro sledování letů v letecké společnosti. Implementujte následující třídy:

Třída Flight:
    Atributy:
        * flight_number (str) - číslo letu
        * current_location (tuple) - aktuální GPS souřadnice letadla
        * flight_status (str) - stav letu ("In Air", "Landed", "Delayed")
        
    Metody:
        * update_location(new_coordinates: tuple) - aktualizuje polohu letadla
        * start_flight() - nastaví stav na "In Air"
        * land_flight() - nastaví stav na "Landed"
        * delay_flight() - nastaví stav na "Delayed"
        * str() - vrátí textovou reprezentaci letu
    
    
Třída CommercialFlight (dědící od Flight):
    Nový atribut:
        * airline (str) - název letecké společnosti
    Nová metoda:
        *   get_flight_info() - vrátí textovou informaci o letu a letecké společnosti
    
    
Třída Airline:
    Atributy:
        * flights (list) - seznam letů ve společnosti (instancí třídy Flight a jejích potomků)
    Metody:
        * add_flight(flight: Flight) - přidá let do společnosti
        * find_flight_by_number(flight_number: str) -> Flight - vyhledá let podle čísla
        * display_airline_status() - zobrazí stav všech letů společnosti
    
Nakonec vytvořte ukázkový příklad, který bude obsahovat vytvoření alespoň 2 letů třídy Flight, 1 letu třídy CommercialFlight a jejich přidání do letecké společnosti a otestujte vytvořené metody.

"""
