## Funkce
Funkce představují skupinu příkazů, které je možné spustit opakovaně více než jednou pomocí volání této funkce. Zjednodušený pohled na funkce je ten, že jsou náhrážkou kopírování stále stejného kódu víckrát. Funkci narozdíl od toho přístupu definujeme jenom jednou.

Jedními z hlavním důvodů pro použití funkcí je:
* znovupoužitelnost kódu a minimalizace redundance
* procedurální dekompozice
  * rozložení postupu (algoritmu) na menší části, které jsou definovány uvnitř funkcí
  * tento postup poté zjednodušuje celý návrh a umožňuje upravovat pouze menší části kódu

Základní syntaxe funkce vypadá následovně:
```python
# funkci definuje klicove slovo def
# nasleduje nazev funkce a v zavorkach seznam argumentu funkce (vstupnich hodnot)
# telo funkce je odsazene 4 mezerami (popr. tabulatorem) a muze obsahovat libovolny pocet prikazu
def name(arg1, arg2,... argN):
    statements
```

Velice částé je také použítí návratové hodnoty z funkce (např. pokud chceme sečíst dvě hodnoty a výsledek vrátit). K tomu slouží klíčové slovo `return`.
```python
# tato funkce na vstupu bere dve promenne number1 a number2 a na vystupu vraci jejich soucet
def addition(number1, number2):
    return number1 + number2

# volani funkce pak vypada nasledovne
# nazev funkce a v zavorce hodnoty
# vysledek se vraci do libovolne promenne nebo ho muzeme treba rovnou vypsat
# promenna result bude obsahovat hodnotu 3
result = addition(1,2)

# nebo vysledek rovnou vypiseme
print(addition(1,2))
```

Pokud nepoužijeme návratovou hodnotu tak funkce vrací hodnotu `None`. `None` představuje prázdnou hodnotu, podobně jako např. `NULL` v databázích. `None` lze také normálně přiřadit do proměnné a zkontrolovat výsledek:
```python
var1 = None
if var1 is None:
    print('Value of var1 is None')
```

Funkce může vracet také více hodnot najednou. V praxi se neděje tak často, ale může se to stát. Například pokud bychom chtěli čísla zároveň sečíst a vynásobit a vrátili dvě hodnoty. Návratový typ je `tuple`.
```python
def sum_and_multiply(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    return sum, mul

print(sum_and_multiply(2, 3))
# vypise
(5, 6)
```

### Kontext proměnné (scope)
Kontext proměnné znamená rozsah, ve kterém je proměnná ještě vidět. Například pokud definujeme proměnnou pouze uvnitř funkce, tak proměnná nebude volatelná z venku funkce, protože po skončení funkce proměnná zanikne.
```python
def add(number1, number2):
    result = number1 + number2
    return result

# vypise NameError: name 'result' is not defined
print(result)
```

Pokud nadefinujeme proměnnou venku z funkce tak se k ní dokážeme dostat i mimo funkci, ale bude obsahovat pouze hodnotu, kterou nastavíme mimo funkci.
Pokud proměnnou definujeme vně funkce, tak k ní můžeme přistupovat i uvnitř funkcí a nemusíme hodnotu předávat jako agumenty funkce.
```python
result = 199

def add(number1, number2):
    print(result)
    return number1+number2

print(add(1,1))

# vypise
# 199
# 2
```

### Defaultní hodnota argumentu
Pokud to dává smysl tak můžeme argumentu nastavit defaultní hodnotu. Tato hodnota pak lze změnit při volání funkce.
```python
# argument number2 bude mít defaultní hodnotu 2
def add2(number1, number2=2):
    return number1+number2

# pri volani funkce muzeme vypustit jeden argument a tim padem number2 pak bude mit hodnotu 2
print(add2(1))
# vypise 3

# argumenty muzeme nastavit i pomoci jejich nazvu funkce
print(add2(1, number2=10))
# vypise 11

# pokud bychom funkci zavolali se dvema parametry, tak number2 nebude mít defaultního hodnotu, ale prebere hodnotu z volani funkce
print(add2(1,1))
# vypise 2
```

### Libovolný počet proměnných
Python umožňuje funkce definovat s libovolným počtem proměnných. Pro tento účel slouží `*` nebo `**`, často v kombinace se slovem `args` nebo `kwargs`.
Jednotlivé hodnoty pak nelze vybírat pmocí názvu argumentu, ale pouze v cyklu nebo přes index. Hodnoty se vlastně předávají jako pole.
```python
def printer(*args):
    for arg in args:
        print(arg)

printer('Ahoj', 'programujeme', 'v', 'Pythonu')
# vypise
# Ahoj
# programujeme
# v
# Pythonu
```

```python
# **kwargs umoznuje posilat pojmenovane parametry (ve forme slovniku)
def printer(**kwargs):
    for key, value in kwargs.items():
        print(key, '=>', value)

printer(first='Ahoj', second='jak', third='to jde')
# vypise
# first => Ahoj
# second => jak
# third => to jde
```


### Typování funkcí
Python patří mezi dynamicky typové jazyky, což znamená, že při vytvoření proměnné neříkáme, jaký typ hodnoty do ní budeme ukládat. Od verze 3.5 ale podporuje typing. Můžeme tedy říct, jaký typ hodnoty by měla obsahovat nějaká proměnná, Python to však nekontroluje a neukončí program s chybou, pokud do proměnné vložíme hodnotu jiného typu. Typování ale funguje jako nápověda pro programátory a především vývojová prostředí, která pak umějí vývojářům lépe napovídat při psaní programů a případně je upozornit, pokud plánují do proměnné vložit něco, co tam nepatří.

Níže je příklad funkce get_mark() s typováním. Typovat můžeme jednotlivé parametry i návratovou hodnotu, jejíž typ je za "šipkou" ->.

```python
def get_mark(points: int, bonus: int = 0) -> int:
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark

print(get_mark(50, 30))
```

### List Comprehension
List Comprehension je elegantní a kompaktní způsob, jak vytvářet seznamy v Pythonu. Umožňuje vytvořit seznam pomocí jednoho řádku kódu, což je často čitelnější a efektivnější než tradiční způsoby vytváření seznamů. List Comprehension využívá jednoduchou syntaxi a lze ho použít pro filtrace, transformaci a vytváření seznamů na základě existujících dat.

Základní syntaxe List Comprehension vypadá takto:

```python
novy_seznam = [vyraz for prvek in stary_seznam if podminka]
```

 - vyraz určuje, jakým způsobem se transformuje prvek ze starého seznamu do nového seznamu.
 - prvek je proměnná, která prochází všechny prvky ze starého seznamu.
 - stary_seznam je původní seznam, ze kterého vytváříme nový seznam.
 - podminka (volitelná) umožňuje filtrovat prvky, které budou zahrnuty do nového seznamu.
 
Nyní můžete vidět, jakým způsobem můžeme použít List Comprehension k vytvoření seznamu obsahujícího druhé mocniny čísel od 1 do 5:

```python
druhe_mocniny = [x**2 for x in range(1, 6)]
print(druhe_mocniny)
# Výstup: [1, 4, 9, 16, 25]
```

List Comprehension umožňuje efektivně pracovat s daty a zkrátit kód, což z něj činí užitečný nástroj pro mnoho běžných úkolů v Pythonu.


### Užitečné funkce
Pokud vám nebude něco jasné, tak si danou funkci vygooglete včetně dalších příkladů použití.
#### `append(obj)`
Přidá prvek na konec seznamu
```python
>>> list1 = [1,2]
>>> list1.append(3)
>>> list1
[1, 2, 3]
```
#### `remove(obj)`
Vymaže první výskyt hledaného prvku
```python
>>> list1.remove(1)
>>> list1
[2, 3]
```

#### `index(obj)`
Vrací první index hledaného prvku
```python
>>> list1
[2, 3]
>>> list1.index(2)
0
```

#### `del list[index]`
Nejedná se o funkci, ale o klíčové slovo. Maže prvek na daném indexu
```python
>>> list1 = [1,2,3,4]
>>> del list1[2]
>>> list1
[1, 2, 4]
```

[Více funkcí k seznamům](https://docs.python.org/3.7/tutorial/datastructures.html)





