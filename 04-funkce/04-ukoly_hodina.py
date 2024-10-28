#Úkol 1
"""Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek."""

def mult(cislo1, cislo2):
    vysledek = cislo1 * cislo2
    return vysledek


print(mult(4, 5))
print(mult(3, 6))
print(mult(40, 70))
    


#Úkol 2
"""Napište funkci vypocet_obvodu_obdelnika, která bude mít dva parametry (délku a šířku) a vrátí obvod obdélníka. o = 2(a+b)"""

def vypocet_obvodu_obdelnika(delka, sirka):
    obvod = 2 * (delka + sirka)
    return obvod

print(vypocet_obvodu_obdelnika(5, 3))




#Úkol 3
"""Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

Zadej slovo: ahoj
********
* ahoj *
********
"""

def obaleni_hvezdickami(text):
    delka = len(text) + 4
    print('*' * delka)
    print(f'* {text} *')
    print('*' * delka)

obaleni_hvezdickami("ahoj")




#Úkol 4
"""Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50."""


def month_of_birth(rodne_cislo):
    mesic = int(rodne_cislo[2:4])
    
    if mesic > 12:
        mesic -= 50
    return mesic

print(month_of_birth("9555121234"))
print(month_of_birth("9303121234"))






