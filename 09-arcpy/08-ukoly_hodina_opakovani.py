# Úkol 1
""" 
Definujte třídu Animal, která bude základní třídou pro modelování různých druhů zvířat. Tato třída by měla mít následující atributy:
 - name (jméno zvířete)
 - species (druh zvířete)
 - age (věk zvířete)

 Dále definujte dvě odvozené třídy, Cat a Dog, které budou odvozeny od třídy Animal. Každá z těchto tříd by měla mít specifické atributy pro každý druh zvířete, například pro Cat to může být atribut "fur_color" a pro Dog "breed". Implementujte konstruktory a metody pro zobrazení informací o zvířeti.
 """ 
 
class Animal:
     def __init__(self, name, species, age):
         self.name = name
         self.species = species
         self.age = age
         
class Cat(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self.fur_color = fur_color
        
    def info_cat(self):
        print(self.name, self.species, self.age, self.fur_color)
        
class Dog(Animal):
    def __init__(self, name, species, age, breed):
        super().__init__(name, species, age)
        self.breed = breed
        
    def info_dog(self):
        print(self.name, self.species, self.age, self.breed)
        
kocka = Cat("Micka", "kočka", 5, "bílá")
pes = Dog("Tom", "pes", 8, "čivava")

kocka.info_cat()
pes.info_dog()
 
# Úkol 2
"""
Vytvořte model pro sledování úkolů v jednoduchém plánovači. Definujte třídu Task s následujícími atributy:
 - title (název úkolu)
 - due_date (termín splnění úkolu)
 - priority (priorita úkolu)

 Dále vytvořte třídu Planner, která bude obsahovat seznam úkolů a metody pro přidání nového úkolu a zobrazení seznamu všech úkolů.

"""

class Task:
    def __init__(self,title,due_date,priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority
    
class Planner:
    def __init__(self):
        self.seznam = []
    
    def pridej(self,ukol):
        self.seznam.append(ukol)
        
    def zobraz(self):
        for i in self.seznam:
            print(i.title)

ukol = Task('seminarka_DPZ','5.12.','1')

planovac = Planner()
planovac.pridej(ukol)
planovac.zobraz()
        
        
    
    