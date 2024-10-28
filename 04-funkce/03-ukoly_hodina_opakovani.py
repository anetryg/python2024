#Úkol 1
"""Napište program, který vezme seznam slov a vytvoří nový seznam, který obsahuje délky těchto slov."""

slova = ["auto", "stůl", "programování"]
delky = []

for slovo in slova:
    delka = len(slovo)
    delky.append(delka)

print(delky)



#Úkol 2
"""Napište program, který vypočítá sinus každého úhlu v seznamu a uloží výsledky do nového seznamu. Použijte metodu sin z knihovny math."""

import math

uhly = [0, 30, 45, 60, 90]
sinusy = []
for uhel in uhly:
    sinus = math.sin(math.radians(uhel))
    sinusy.append(sinus)

print(sinusy)


#Úkol 3
"""Napište program, který generuje 10 náhodných čísel a poté vytvoří seznam těch čísel, která jsou menší než 0.5."""

import random

nahodna_cisla = []
mensi_nez_pul = []
for _ in range(10):
    cislo = random.random()
    nahodna_cisla.append(cislo)
    if cislo < 0.5:
        mensi_nez_pul.append(cislo)

print("Generovaná čísla:", nahodna_cisla)
print("Čísla menší než 0.5:", mensi_nez_pul)




#Úkol 4
"""Uvažujme vysvědčení, které máme zapsané jako slovník.

Napiš program, který spočte průměrnou známku ze všech předmětů.
Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1."""

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

vysvedceni = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

soucet_znamek = 0
pocet_predmetu = 0
for predmet, znamka in vysvedceni.items():
    soucet_znamek += znamka
    pocet_predmetu += 1

prumerna_znamka = soucet_znamek / pocet_predmetu
print("Průměrná známka:", prumerna_znamka)

predmety_se_znamkou_1 = []
for predmet, znamka in vysvedceni.items():
    if znamka == 1:
        predmety_se_znamkou_1.append(predmet)

print("Předměty se známkou 1:", predmety_se_znamkou_1)



