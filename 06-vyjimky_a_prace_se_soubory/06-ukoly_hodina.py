# Úkol 1
""" Napište program, který bude očekávat od uživatele dva parametry. Parametry mohou být celá nebo desetinná čísla. Vypiš podíl těchto čísel. Ošetři, aby program nezhavaroval při pokusu o dělení nulou. """

try:
    cislo = float(input("Zadejte číslo: "))
    cislo2 = float(input("Zadejte druhé číslo: "))
    
    print(cislo / cislo2)
except ZeroDivisionError:
    print("Nemůžete dělit nulou!")




# Úkol 2
""" Vytvořte pomocí pythonu textový soubor vykaz.txt, který bude obsahovat 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok."""

with open('vykaz.txt', 'w') as file:
    for line in range(12):
        file.write(f"10 20 15 5 1 7 16\n")
        
    

# Úkol 3
""" Napište program, který se po spuštění zeptá na název souboru, který má vytvořit (nebo přepsat, pokud už ten soubor existuje), a pak se zeptá na řádek textu, který má do souboru zapsat. """

nazev = input("Zadejte název souboru:")

with open(nazev, 'w') as file:
    file.write(input("Zadejte řádek textu:"))
    

# Úkol 4
""" Napište program, který vytvoří textový soubor s názvem "nákupní_seznam.txt". Program se bude opakovaně ptát uživatele na položky k přidání do nákupního seznamu, dokud uživatel nezadá prázdný řetězec. Každá položka by měla být uložena na nový řádek v souboru.
"""

with open('nakupni_seznam.txt','w') as file:
    while True:
        poznamky=input('Zadej nakup: ')
        if poznamky=='':
            break
        else: 
            file.write(f"{poznamky}\n")

# Úkol 5
""" Napište program, který umožní uživateli zkopírovat obsah jednoho souboru do druhého. Program by měl zeptat se na názvy zdrojového a cílového souboru a poté přečíst obsah z jednoho souboru a zapsat ho do druhého.
"""

odkud = input('Odkud chceš kopírovat text? ')
kam = input('a kam ko chceš zkopírovat? ')

with open(odkud,'r') as zdroj:
    text = zdroj.read()
    with open(kam,'w') as cil:
        cil.write(text)

