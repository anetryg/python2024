## 1. bodovaný úkol
Vytvořte textovou hru (https://en.wikipedia.org/wiki/Text-based_game), kde využijete větvení pomocí podmínek. Nezapomeňte také použít datové typy list a dictionary (slovník například pro vyběr voleb uživatele). Fantazii se meze nekladou.

## Cykly
Cykly v programování slouží k opakování určitých operací. Pomocí cyklu můžete například prohledávat pole a zastavit cyklus ve chvíli, kdy narazíte na hledaný prvek. Nebo můžete například vypsat postupně název všech studentů apod.

### Cyklus for
Cyklus for se používá pro procházení jakékoliv uspořádané nebo iterovatelné struktury (třeba seznam, slovník apod.). Jedná se pravděpodobně o častěji používáný cyklus než while.
```python
for x in ["spam", "eggs", "ham"]:
    print(x)
# vypise spam eggs ham
```

Proměnná `x` představuje proměnnou, která v sobě bude uchovávat hodnotu z pole (vždy jen jednu pro jeden průchod). Stejně tak můžeme v cyklu třeba sčítat hodnoty.
```python
for x in [1, 2, 3, 4]:
    sum = sum + x
```

Pokud budeme chtít iterovat přes slovník, tak je potřeba určit jestli budeme iterovat jen přes klíče nebo budeme chtít iterovat i přes hodnoty.
```python
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key)                  # vypise klic
    print(D[key])               # vypise hodnotu

# pokud budeme chtit iterovat i pres hodnotu
for (key, value) in D.items():
    print(key, '=>', value)
```

Cykly mohou být zanořené stejně jako podmínky.
```python
items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
        else:
            print(key, "not found!")

# Vypise
#(4, 5) was found
#3.14 not found!
```

Pokud chcete iterovat předem daným počtem opakování, musíte použít funkci **range()**:
```python
for i in range(0,3):
    print(i)
# Vypise
# 0
# 1
# 2
```

### Cyklus while
While cyklus provádí určitou operaci dokud je splněna podmínka, která se nachází na začátku cyklu.
```python
>>> while True:
...    print('Type Ctrl-C to stop me!')
```
Cyklus nikdy neskončí, protože podmínka je vždy True. Ukončení může provést uživatel pomocí Ctrl-C nebo cyklus skončí na maximálním možném počtu průchodů.

```python
a=0; b=10               # definovat promenne muze i na jednom radku
while a < b:
    print(a, end=' ')
    a += 1              # stejny zapis jako a = a + 1
# vysledek bude 0 1 2 3 4 5 6 7 8 9
```

Klíčové slovo **break** může ukončit cyklus pokud nastane určitá podmínka.
```python
while True:
    name = input('Enter name:')
    if name == 'stop':
        break
    age = input('Enter age: ')

    # input() vraci hodnotu typu string takze pro vypocet musime hodnotu prevest na integer
    print('Hello', name, '=>', int(age) ** 2)
```



### Importy
Importy slouží k nahrání jiného kódu (knihovny) do toho vašeho. Knihovny jsou části kódu, které napsal někdo před vámi, protože chtěl rozšířit nějakou funkcionalitu. Sám Python obsahuje zabudované knihovny pro různé použití. Existují však i knihovny neoficiální, které lze najít na internetu. Jedním z managerů, kde lze najít knihovny na jednom místě je [pip](https://pypi.org/). My si na začátek vyzkoušíme vygenerování náhodného čísla.
```python
# pro generovani nahodnych cisel slouzi knihovna random
# nejdrive naimportujeme kod (knihovnu) pomoci klicoveho slova import a nazvu knihovny
import random

# pote muzeme zavolat funkci randint(), ktera vygeneruje nahodny integer
# volani funkce musi predchazet i balicek, ve kterem je funkce obsazena (random)
print(random.randint(1, 21))

# pokud bychom chteli vynechat random ve volani funkce, tak muzeme naimportovat jen funkci
from random import randint
print(randint(1, 21))
```

Jeden z užitečných modulů nese název math, a obsahuje mnoho standardních matematických funkcí. Mimo jiné obsahuje funkce pro zaokrouhlování nahoru a dolů. Pokud chceme modul math použít, musíme jej nejdříve importovat příkazem

```python
import math
```

Příkazy import pro přehlednost zapisujeme na začátek programu. Poté, co tento příkaz zadáme Pythonu, můžeme volat všechny funkce z tohoto modulu tak, že vždy před název funkce pomocí tečky připojíme název modulu, ze kterého funkce pochází. Například

```python
zaokrouhlene_cislo = math.ceil(3.14)
print(zaokrouhlene_cislo)
```


