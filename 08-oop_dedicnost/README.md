# Dědičnost v OOP
Dědičnost je klíčovým konceptem v objektově orientovaném programování (OOP), který umožňuje vytvářet nové třídy na základě existujících tříd. Tato vlastnost umožňuje znovupoužívání kódu, abstrakci a hierarchii tříd.

Uvažujme situaci, kdy chceme vytvořit novou třídu s názvem Manager, která reprezentuje zaměstnance s podřízenými. Tato třída by měla obsahovat informaci o počtu podřízených. Zároveň by měla sdílet vlastnosti s třídou Employee, jako jsou jméno, pozice a nárok na dovolenou.

Namísto opisování kódu z třídy Employee a jeho upravování pro novou třídu Manager, můžeme využít dědičnost. Vytvoříme tedy třídu Manager jako dceřinou třídu třídy Employee. Tím získáme všechny atributy a metody z třídy Employee, a můžeme pouze přidat nebo upravit, co potřebujeme.

```python
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates

    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízených."
```

Vytvořili jsme novou metodu __init__ pro třídu Manager, kde jsme pomocí super() zavolali metodu __init__ z mateřské třídy Employee. Tím jsme převzali inicializační část kódu a přidali atribut subordinates pro novou třídu.

Také jsme přidali vlastní implementaci metody __str__, kde jsme znovu pomocí super() zavolali metodu __str__ z mateřské třídy Employee a připojili k výsledku informaci o počtu podřízených.

Nyní můžeme vytvářet instance třídy Manager a využívat dědičnost pro sdílení a rozšiřování funkcionalit.

```python
boss = Manager("Pavel Novák", "vedoucí oddělení", 25, 5)
print(boss)
```

Tímto způsobem efektivně využíváme dědičnost a sdílíme kód mezi třídami Employee a Manager, zároveň umožňujeme specifické úpravy pro třídu Manager.

## Nepovinné parametry
Nyní si představme, že chceme rozšířit naši třídu Employee o další informaci, například registrační značku služebního auta (car_license_plate). U většiny zaměstnanců není služební auto k dispozici, a proto bychom chtěli, aby tato informace byla nepovinná. V Pythonu můžeme použít hodnotu None k označení prázdné hodnoty. Abychom si ušetřili práci, můžeme parametr license_plate přidat do metody __init__ jako nepovinný, nastavující se na výchozí hodnotu None. Stejným způsobem nastavíme i parametr holiday_entitlement, protože předpokládáme, že ve většině případů bude mít hodnotu 25.

Při vytváření objektu můžeme zadat hodnoty pouze pro povinné parametry. Pokud neposkytneme hodnoty pro nepovinné parametry, budou použity výchozí hodnoty.

```python
class Employee:
    def __init__(self, name, position , holiday_entitlement=25, car_license_plate=None):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.car_license_plate = car_license_plate
    
    def __str__(self):
        text = f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
        if self.car_license_plate:
            text += f" Má k dispozici služební auto {self.car_license_plate}."
        return text

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

frantisek = Employee("František Novák", "konstruktér")
print(str(frantisek))
print(frantisek.take_holiday(15))
print(frantisek.take_holiday(15))
```

Nyní předpokládejme, že chceme přidat zaměstnankyni, která má služební auto, ale standardních 25 dní dovolené. Parametr holiday_entitlement můžeme přeskočit tím, že hodnotu parametru car_license_plate zadáme včetně názvu. Název je nezbytný, protože kdybychom zadali pouze registrační značku, Python by ji uložil do atributu holiday_entitlement. Při volání metody take_holiday by poté program skončil chybou.

```python
natalie = Employee("Natálie Novotná", "sales manažerka", car_license_plate="1P7 4774")
print(str(natalie))
print(natalie.take_holiday(15))
print(natalie.take_holiday(15))
```

Tímto způsobem můžeme efektivně vytvářet instance třídy Employee, přičemž můžeme využít výchozí hodnoty pro nepovinné parametry a zadávat hodnoty s využitím pojmenovaných argumentů, což přispívá k čitelnosti kódu.

## Speciální metody
V Pythonu existuje skupina speciálních metod, známých jako dunder (double underscore), které umožňují definovat specifické chování objektů v různých kontextech. Tyto metody mají v syntaxi názvy s dvojitými podtržítky (například __init__)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(str(p))  # Tato operace automaticky zavolá metodu __str__.
```

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4])
print(len(my_list))  # Tato operace automaticky zavolá metodu __len__.
```

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)  # Tato operace automaticky zavolá metodu __eq__.
```

```python
class MyContainer:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

container = MyContainer([1, 2, 3, 4])
print(container[2])  # Tato operace automaticky zavolá metodu __getitem__.
```

Příklady ukazují, jak můžete tyto metody implementovat pro vlastní třídy a jak mohou být využity ve standardních operacích a funkcích v jazyce Python.

### Initialization and Construction
* __new__: To get called in an object’s instantiation.
* __init__: To get called by the __new__ method.
* __del__: It is the destructor.

### Numeric magic methods
* __trunc__(self): Implements behavior for math.trunc()
* __ceil__(self): Implements behavior for math.ceil()
* __floor__(self): Implements behavior for math.floor()
* __round__(self,n): Implements behavior for the built-in round()
* __invert__(self): Implements behavior for inversion using the ~ operator.
* __abs__(self): Implements behavior for the built-in abs()
* __neg__(self): Implements behavior for negation
* __pos__(self): Implements behavior for unary positive 

### Arithmetic operators
* __add__(self, other): Implements behavior for math.trunc()
* __sub__(self, other): Implements behavior for math.ceil()
* __mul__(self, other): Implements behavior for math.floor()
* __floordiv__(self, other): Implements behavior for the built-in round()
* __div__(self, other): Implements behavior for inversion using the ~ operator.
* __truediv__(self, other): Implements behavior for the built-in abs()
* __mod__(self, other): Implements behavior for negation
* __divmod__(self, other): Implements behavior for unary positive 
* __pow__: Implements behavior for exponents using the ** operator.
* __lshift__(self, other): Implements left bitwise shift using the << operator.
* __rshift__(self, other): Implements right bitwise shift using the >> operator.
* __and__(self, other): Implements bitwise and using the & operator.
* __or__(self, other): Implements bitwise or using the | operator.
* __xor__(self, other): Implements bitwise xor using the ^ operator.

### String Magic Methods
* __str__(self): Defines behavior for when str() is called on an instance of your class.
* __repr__(self): To get called by built-int repr() method to return a machine readable representation of a type.
* __unicode__(self): This method to return an unicode string of a type.
* __format__(self, formatstr): return a new style of string.
* __hash__(self): It has to return an integer, and its result is used for quick key comparison in dictionaries.
* __nonzero__(self): Defines behavior for when bool() is called on an instance of your class. 
* __dir__(self): This method to return a list of attributes of a class.
* __sizeof__(self): It return the size of the object.

### Comparison magic methods
* __eq__(self, other): Defines behavior for the equality operator, ==.
* __ne__(self, other): Defines behavior for the inequality operator, !=.
* __lt__(self, other): Defines behavior for the less-than operator, <.
* __gt__(self, other): Defines behavior for the greater-than operator, >.
* __le__(self, other): Defines behavior for the less-than-or-equal-to operator, <=.
* __ge__(self, other): Defines behavior for the greater-than-or-equal-to operator, >=.

## Datové třídy
V Pythonu 3.7 a novějších verzích byly přidány datové třídy (dataclass), které umožňují automatické vytváření metody __init__ pro inicializaci objektů. Tím se eliminuje potřeba opakovaně psát boilerplate kód. Název "boilerplate" je převzatý z kovových štítků na bojlerech, které obsahují standardní informace a nemění se často.

Pomocí datových tříd vytváříme struktury dat s minimálním množstvím kódu. Specifikujeme atributy a jejich typy přímo ve třídě a můžeme dokonce přidat výchozí hodnoty.

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    position: str
    holiday_entitlement: int = 25

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."
```

použití datové třídy:

```python
frantisek = Employee("František Novák", "konstruktér")
print(frantisek.take_holiday(5))
print(frantisek.take_holiday(15))
print(frantisek.take_holiday(10))
```

V tomto příkladu máme třídu Employee, která je označena jako datová třída pomocí dekorátoru @dataclass. Atributy name, position a holiday_entitlement jsou jednoduše deklarovány se svými typy. Navíc máme atribut holiday_entitlement s výchozí hodnotou 25.

Díky tomu nemusíme explicitně implementovat metodu __init__, a třída bude automaticky vygenerována s touto metodou a dalšími užitečnými metodami, jako například __repr__ pro reprezentaci objektu v řetězci. Datové třídy tak usnadňují práci s objekty a zjednodušují kód.

## Soukromé atributy a metody
V Pythonu lze označit atributy a metody jako soukromé přidáním dvojitých podtržítek na začátek jejich názvu (např. __private_attribute). Soukromé atributy a metody jsou pak přístupné pouze uvnitř dané třídy a neměly by být přímo volány z vnějšku. Tento přístup umožňuje skrýt implementační detaily a chránit data třídy.

Atribut __holiday_entitlement ze třídy Employee se po spuštění pro veřejnost přemění na _Employee__holiday_entitlement a pro svou instanci zůstane jako __holiday_entitlement. Díky tomuto nedojde v dědící třídě k přejmenování pomocných funkcí, které jsou zásadní pro fungování ostatních funkcí. I tyto funkce se nezobrazí po dosazení třídy nebo instance do napovídající funkce help.

```python
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.__holiday_entitlement = holiday_entitlement
    
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):
        if self.__holiday_entitlement >= days:
            self.__holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.__holiday_entitlement} dní."

frantisek = Employee("František Novák", "konstruktér", 25)
print(str(frantisek))

# print(frantisek.__holiday_entitlement) # chyba
print(frantisek._Employee__holiday_entitlement)
```

Opět je třeba zdůraznit, že Python je poměrně specifický v tom, že nemá opravdové soukromé atributy. Většina programovacích jazyků rozlišuje mezi veřejnými (public) a soukromými (private) atributy a neexistuje žádný "trik", jak s nimi pracovat mimo metody dané třídy.

![Alt text](https://github.com/anetryg/python2023/blob/main/08-oop_dedicnost/images/private_method.PNG)


## Výhody OOP?

Základní příklad a srovnání přístupů:

```python
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"{self.name} - {self.position}, Salary: ${self.salary}")

    def increase_salary(self, percentage):
        self.salary *= (1 + percentage / 100)
        print(f"{self.name}'s salary increased to ${self.salary}")


# Vytvoření zaměstnanců
employee1 = Employee("John Doe", "Developer", 50000)
employee2 = Employee("Jane Smith", "Manager", 60000)

# Zobrazení informací o zaměstnancích
employee1.display_info()
employee2.display_info()

# Zvýšení platu zaměstnance o 10%
employee1.increase_salary(10)
```

```python
def create_employee(name, position, salary):
    return {"name": name, "position": position, "salary": salary}

def display_info(employee):
    print(f"{employee['name']} - {employee['position']}, Salary: ${employee['salary']}")

def increase_salary(employee, percentage):
    employee['salary'] *= (1 + percentage / 100)
    print(f"{employee['name']}'s salary increased to ${employee['salary']}")


# Vytvoření zaměstnanců
employee1 = create_employee("John Doe", "Developer", 50000)
employee2 = create_employee("Jane Smith", "Manager", 60000)

# Zobrazení informací o zaměstnancích
display_info(employee1)
display_info(employee2)

# Zvýšení platu zaměstnance o 10%
increase_salary(employee1, 10)
```

Rozšíření příkladu a srovnání přístupů:

```python
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"{self.name} - {self.position}, Salary: ${self.salary}")

    def increase_salary(self, percentage):
        self.salary *= (1 + percentage / 100)
        print(f"{self.name}'s salary increased to ${self.salary}")


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Manager", salary)

    def promote_team_member(self, employee):
        print(f"{self.name} promoted {employee.name} to a higher position")


# Vytvoření zaměstnanců a manažera
employee1 = Employee("John Doe", "Developer", 50000)
employee2 = Employee("Jane Smith", "Developer", 55000)
manager = Manager("Bob Johnson", 70000)

# Zobrazení informací o zaměstnancích
employee1.display_info()
employee2.display_info()
manager.display_info()

# Zvýšení platu zaměstnance o 10%
employee1.increase_salary(10)

# Manažer povýší zaměstnance
manager.promote_team_member(employee2)
```

```python
def create_employee(name, position, salary):
    return {"name": name, "position": position, "salary": salary}

def display_info(employee):
    print(f"{employee['name']} - {employee['position']}, Salary: ${employee['salary']}")

def increase_salary(employee, percentage):
    employee['salary'] *= (1 + percentage / 100)
    print(f"{employee['name']}'s salary increased to ${employee['salary']}")

def promote_team_member(manager, employee):
    print(f"{manager['name']} promoted {employee['name']} to a higher position")


# Vytvoření zaměstnanců a manažera
employee1 = create_employee("John Doe", "Developer", 50000)
employee2 = create_employee("Jane Smith", "Developer", 55000)
manager = create_employee("Bob Johnson", "Manager", 70000)

# Zobrazení informací o zaměstnancích
display_info(employee1)
display_info(employee2)
display_info(manager)

# Zvýšení platu zaměstnance o 10%
increase_salary(employee1, 10)

# Manažer povýší zaměstnance
promote_team_member(manager, employee2)
```

V příkladu bez OOP je funkce pro povýšení zaměstnance (promote_team_member) přístupná všem, a není ničím omezeno, kdo ji může volat. Může ji použít kdokoli, kdo má přístup k této funkci.

Naopak v OOP příkladu s třídami a dědičností je metoda promote_team_member specifická pro třídu Manager. Pouze instance této třídy (tj. manažeři) budou moci volat tuto metodu. To poskytuje jistou úroveň omezení přístupu, což může být užitečné v situacích, kdy chcete specifikovat, kdo může vykonávat určité operace v rámci objektů určité třídy.




