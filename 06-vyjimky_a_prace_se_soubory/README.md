## Výjimky
Výjimky (exceptions) umožňují v případě chyby nebo nějaké situace přeskočit část kódu, popřípadě úplně zastavit běh programu.

Situace, ve kterých je použijeme:
* ošetření chyb
* oznámení události
* ošetření situací, které mohou nastat velmi zřídka
* provedení ukončovací akce

S výjimkami jste se už setkali v případě chyb, např. pokud budu dělit 0, tak Python vypíše výjimku ZeroDivisionError.
```python
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Pokud bychom chtěli, aby program nespadl v případě, že budeme dělit 0, ale chceme nějak na dělení 0 zareagovat, tak můžeme použít konstrukci `try`
```python
try:
    var = 1/0
except ZeroDivisionError:
    print('Nemuzes delit 0')
# vypise Nemuzes delit 0
```
V tomhle případě program nespadne na chybě, ale protože jsme se situací počítali, tak na ni zareagujeme varováním o tom, že nemůžeme dělit 0. Program normálně doběhne do konce.
Try můžeme použít všude, kde lze očekávat nějakou chybu. Za klíčovým slovem except následuje název výjimky. Více jich je [zde](https://docs.python.org/3.7/library/exceptions.html).
Můžeme sice použít situaci, kdy ošetříme všechny výjimky, ale tento přístup se moc nedoporučuje, protože se může stát situace, že ošetříme situaci, se kterou jsme nepočítali a nedozvíme se o chybě.
```python
try:
    var = 1/0
except:                     # odchytne vsechny vyjimky
    print('Nemuzes delit 0')

try:
    var = 1/0
except (ZeroDivisionError, ValueError):   # odchytne jen dve zadane vyjimky
    print('Nemuzes delit 0')
```

Pokud bychom chtěli, aby program skončil, ale budeme chtít zobrazit konkrétní chybu, tak můžeme použít klíčové slovo `raise`, které vyhodí konkrétní výjimku.
```python
var1 = 1
var2 = 0

if var2 == 0:
    raise ZeroDivisionError('Nemuzes delit 0')

print(var1/var2)
# vypise
# Traceback (most recent call last):
# File "/home/bulva/PycharmProjects/python-2020/06-vyjimky_a_prace_se_soubory/test.py", line 5, in <module>
#   raise ZeroDivisionError('Nemuzes delit 0')
# ZeroDivisionError: Nemuzes delit 0
```

### Více except bloků
V případě potřeby můžete mít více except bloků pro různé typy výjimek a zacházet s nimi specificky.

```python
try:
    # něco, co může vyvolat výjimku
except ZeroDivisionError:
    # reakce na dělení nulou
except ValueError:
    # reakce na hodnotovou chybu
except Exception as e:
    # obecný blok pro zachycení jakékoliv výjimky
    print(f"Neočekávaná chyba: {e}")
```

### Blok else s try a except
Můžete také použít blok else s try a except, který se vykoná, pokud nevznikne žádná výjimka.

```python
try:
    # něco, co by mohlo způsobit výjimku
except SomeException:
    # provede se, pokud vznikne výjimka
else:
    # provede se, pokud žádná výjimka nenastane
```

### Blok finally
Blok finally obsahuje kód, který se vykoná vždy, bez ohledu na to, zda došlo k výjimce nebo ne. Například pro uvolnění zdrojů nebo provedení závěrečných úkonů.

```python
try:
    # něco, co může vyvolat výjimku
except SomeSpecificException:
    # reakce na konkrétní výjimku
finally:
    # tento kód se vždy provede, bez ohledu na výjimku
```

## Práce se soubory
Práce se soubory v Pythonu je extrémně jednoduchá. Pro práci se soubory (jejich otevření) se používá funkce `open()`.
```python
# otevre soubor
myfile = open('myfile.txt', 'w')

# zapise do souboru
myfile.write('hello text file\n')

# zavre soubor
myfile.close()
```

První argument funkce `open()` je název (nebo cesta) k souboru. Druhý argument je režim:
* r - otevření souboru pro čtení
* w - otevření souboru pro zápis (přepíše obsah)
* a - otevření souboru pro přidání textu na konec souboru

```python
myfile = open('myfile.txt') # defaultni rezim je 'r'
print(myfile.readline()) # prectu radek
```

Soubor můžeme číst i po řádku.
```python
for line in open('myfile.txt'):
    print(line, end='')

# vypise 1. radek
# vypise 2. radek atd.
```

Python3 umožňuje použít funkci `open()` s klíčovým slovem with, které po ukončení bloku zavře soubor.
```python
with open('myfile.txt') as file:
    read_data = file.read()
# zde je soubor uz uzavreny
```

Při čtení nebo zápisu textových souborů můžete specifikovat kódování, např. 'utf-8'

```python
with open('myfile.txt', 'r', encoding='utf-8') as file:
    data = file.read()
```

### Kódování

Kódování je proces převádění znaků lidského jazyka na sérii čísel, která může být reprezentována v binární podobě. Znaky v počítači jsou převáděny na čísla podle určitého schématu, které je známo jako kódování znaků. Existuje mnoho různých kódování, která umožňují reprezentaci znaků různých jazyků a symbolů.

Unicode je mezinárodní standard pro kódování znaků, který přiděluje jedinečné číslo každému znaku a symbolu, nezávisle na platformě, softwaru nebo jazyce. Tím se překonávají problémy s nekompatibilitou kódování, které v minulosti vedly k problémům s přenosem textu mezi různými systémy. Unicode poskytuje systém pro přiřazování kódových bodů různým znakům, zatímco UTF-8 poskytuje způsob, jak tyto kódové body reprezentovat v binární formě. UTF-8 je jedním z několika způsobů kódování Unicode.

Další funkce pro práci se soubory

![file functions](https://gitlab.com/Bulva/python-2020/raw/master/06-vyjimky_a_prace_se_soubory/images/files.png)
