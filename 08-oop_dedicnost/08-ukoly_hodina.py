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

class Shape:
    def __init__(self, color="white", filled=True):
        self.color = color
        self.filled = filled

    def display_info(self):
        if self.filled:
           return f"Tvar je vyplněný a barva: {self.color}."
        else:
            return f"Tvar není vyplněný a barva: {self.color}."

    def calculate_area(self):
        pass



# Úkol 2
""" Od třídy Shape odvoďtě třídy Rectangle a Circle.

Třída Rectangle by měla mít následující atributy:
- length (délka obdélníka)
- width (šířka obdélníka)

Třída Circle by měla mít následující atributy:
- radius (poloměr kruhu)

Obě třídy by měly přepsat metodu calculate_area pro konkrétní výpočet obsahu pro každý tvar.
"""

class Rectangle(Shape):
    def __init__(self, length, width, color="white", filled=True):
        super().__init__(color, filled)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius, color="white", filled=True):
        super().__init__(color, filled)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

rectangle = Rectangle(5, 10, color="blue", filled=False)
circle = Circle(7, color="red")

print(rectangle.display_info())
print(f"Obsah obdélníka: {rectangle.calculate_area()}")

print(circle.display_info())
print(f"Obsah kruhu: {circle.calculate_area()}")




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


class ClothingItem:
    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        return f"{self.name} (Velikost: {self.size}, Barva: {self.color}, Cena: {self.price} Kč)"

    def calculate_discounted_price(self, discount_percentage):
        discounted_price = self.price * (1 - discount_percentage / 100)
        return round(discounted_price, 2)


    
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

class TShirt(ClothingItem):
    def __init__(self, name, size, color, price, fabric):
        super().__init__(name, size, color, price)
        self.fabric = fabric

    def add_logo(self, logo):
        print(f"Logo '{logo}' bylo přidáno na tričko {self.name}.")

class Pants(ClothingItem):
    def __init__(self, name, size, color, price, fit):
        super().__init__(name, size, color, price)
        self.fit = fit

    def adjust_length(self, new_length):
        print(f"Délka kalhot {self.name} byla upravena na {new_length} cm.")

        

tshirt = TShirt("Tričko", "L", "černá", 499, "bavlna")
tshirt.add_logo("Nike")
print(tshirt.display_info())
print(f"Cena po slevě: {tshirt.calculate_discounted_price(20)} Kč")

pants = Pants("Džíny", "32", "modrá", 1299, "slim fit")
pants.adjust_length(90)
print(pants.display_info())
