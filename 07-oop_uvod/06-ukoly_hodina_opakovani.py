#Úkol 1
"""Napište program, který bude přijímat vstup od uživatele a ukládat ho do textového souboru. Program by měl ošetřit situaci, kdy dojde k chybě při zápisu do souboru (IOError)."""

try:
    with open("ukol_1.txt", "w") as file:
        poznamka = input("Napiš něco: ")
        file.write(poznamka)
except IOError:
    print("Pozor! Špatně zadaná cesta k souboru")


#Úkol 2
"""Napište program, který umožní uživateli zadat název existujícího textového souboru a poté vypíše, zda je soubor prázdný nebo ne (FileNotFoundError). """

try:
    with open("ukol_12.txt", "r") as file:
        if file.read() == "":
            print("Prázdný soubor.")
        else:
            print("Soubor není prázdný.")
except FileNotFoundError:
    print("soubor neexistuje")


#Úkol 3
"""Vytvořte program, který umožní uživateli přidávat další řádky do existujícího textového souboru. Program by měl nejprve načíst obsah souboru a poté umožnit uživateli přidávat nové řádky."""

file_name = input("Zadej název souboru: ")

with open(file_name,"a+") as file:
    file.seek(0)  # Přesun kurzoru na začátek souboru
    print(file.read())
    file.write(input("Zadej text: "))

