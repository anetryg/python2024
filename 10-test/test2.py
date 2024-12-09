"""
    * Na zpracování máte 60 minut.
    * Celkově je možné získat 40 bodů.
    * Odevzdávejte do odevzdávárny v isu jako jeden .py soubor.


Vaším úkolem bude vytvořit program pro sledování polohy vozidel v prostoru. Implementujte následující třídy:

Třída Vehicle:
    Atributy:
        * registration_number (str) - registrační číslo vozidla
        * current_location (tuple) - aktuální GPS souřadnice vozidla
        * movement_status (str) - stav pohybu vozidla ("Moving" nebo "Stopped"), který bude defaultně nastaven náhodně pomocí knihovny random - random.choice(["Moving", "Stopped"])
    Metody:
        * update_location(new_coordinates: tuple) - aktualizuje polohu vozidla
        * start_movement() - nastaví stav pohybu na "Moving"
        * stop_movement() - nastaví stav pohybu na "Stopped"
        * __str__(): str - vrátí textovou reprezentaci objektu
        
Třída TrackedVehicle (dědící od Vehicle):
    Nový atribut:
        * tracking_system (str) - typ sledovacího systému (např., "GPS", "Satellite")
    Nová metoda:
        * display_tracking_info(): str - vrátí textovou informaci o sledovacím systému
        
Třída Fleet:
    Atributy:
        * vehicles (list) - seznam vozidel ve flotile (instancí třídy Vehicle a jejích potomků)
    Metody:
        * add_vehicle(vehicle: Vehicle) - přidá vozidlo do flotily
        * find_vehicle_by_registration(registration_number: str) -> Vehicle - vyhledá vozidlo podle registračního čísla
        * display_fleet_status() - zobrazí aktuální stav pohybu všech vozidel ve flotile

Nakonec vytvořte ukázkový příklad, který bude obsahovat vytvoření alespoň 2 vozidel třídy Vehicle, 1 vozidla třídy TrackedVehicle a jejich přidání do flotily a otestujte vytvořené metody.
"""
