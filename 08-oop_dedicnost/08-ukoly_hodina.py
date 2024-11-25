import math

# Úkol 1
""" Uvažujme, že chceme modelovat různé geometrické tvary jako čtverec, kruh a obdélník. Využijeme dědičnosti k vytvoření obecné třídy Shape.
 
Třída Shape by měla mít následující atributy:
- color (barva tvaru, defaultně nastavena na "white")
- filled (informace o tom, zda je tvar vyplněný, defaultně True)

Třída Shape by měla mít následující metody:
- __init__(self, color="white", filled=True): konstruktor třídy.
- display_info(self): Metoda pro zobrazení informací o tvaru.
- calculate_area(self): Metoda pro výpočet obsahu tvaru (metoda s pass, určená k přepsání v odvozených třídách).
"""
    



# Úkol 2
""" Od třídy Shape odvoďtě třídy Rectangle a Circle.

Třída Rectangle by měla mít následující atributy:
- length (délka obdélníka)
- width (šířka obdélníka)

Třída Circle by měla mít následující atributy:
- radius (poloměr kruhu)

Obě třídy by měly přepsat metodu calculate_area pro konkrétní výpočet obsahu pro každý tvar.
"""



# Úkol 3
""" Uvažujme online obchod s oblečením, kde máme různé typy oblečení, jako jsou trička, kalhoty a bundy. Použijeme dědičnost k vytvoření obecné třídy ClothingItem - a od ní odvozených tříd pro konkrétní typy oblečení.

Třída ClothingItem by měla mít následující atributy:
- name (název oblečení)
- size (velikost oblečení)
- color (barva oblečení)
- price (cena oblečení v korunách)

Třída ClothingItem by měla mít následující metody:
- __init__(self, name, size, color, price): Konstruktor třídy.
- display_info(self): Metoda pro zobrazení informací o kusu oblečení.
- calculate_discounted_price(self, discount_percentage): Metoda pro výpočet slevy na cenu oblečení."""




    
# Úkol 4
""" Od třídy ClothingItem odvoďtě třídy TShirt a Pants.

Třída TShirt by měla mít následující atributy:
- fabric (typ látky trička)

Třída Pants by měla mít následující atributy:
- fit (střih kalhot)

Metody pro třídu TShirt:
- add_logo(self, logo): Simuluje přidání loga na tričko.

Metody pro třídu Pants:
- adjust_length(self, new_length): Simuluje úpravu délky kalhot na novou délku.

"""


        


