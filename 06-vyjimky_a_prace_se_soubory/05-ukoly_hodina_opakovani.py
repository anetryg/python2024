# Úkol 1
"""Napište funkci nahrad_samohlasky, která bude mít jeden parametr (řetězec) a nahradí všechny samohlásky ve slově znakem '-'. Funkce vrátí upravený řetězec. 

"""

def nahrad_samohlasky(retezec):
    samohlasky = "aeiouy"
    vysledek = "" 
    for pismeno in retezec: 
        if pismeno in samohlasky:
            vysledek += '-' 
        else: 
            vysledek += pismeno 
    return vysledek
print(nahrad_samohlasky('ahoj'))

# Úkol 2
"""Napište funkci secti_prvni_a_posledni, která bude mít jako parametr seznam čísel. Funkce sečte první a poslední prvek seznamu a vrátí výsledek."""

def secti_prvni_a_posledni(seznam):
    firstlast = seznam[0] + seznam[-1]
    return firstlast

vysledek = secti_prvni_a_posledni([1, 2, 3, 4, 5, 6])
print(vysledek)


# Úkol 3
"""Napište funkci overeni_hesla, která bude mít jeden parametr (heslo). Funkce ověří, zda heslo splňuje následující podmínky:
- Je dlouhé alespoň 8 znaků
- Obsahuje alespoň jedno velké písmeno
- Obsahuje alespoň jedno malé písmeno
- Obsahuje alespoň jedno číslo
Funkce vrátí True, pokud heslo splňuje všechny podmínky, jinak vrátí False. Použijte isupper() - kontrola velkého písmena, islower() - kontrola malého písmena, isdigit() - kontrola čísla."""
            
            

def overenie_hesla(heslo):
    if len(heslo) < 8: 
        return False
    velkepismeno = False
    malepismeno = False
    cislo = False
    
    for pismeno in heslo:
        if pismeno.isupper():
            velkepismeno = True
        if pismeno.islower():
            malepismeno = True
        if pismeno.isdigit():
            cislo = True    
            
    if velkepismeno == True:
        if malepismeno == True:
            if cislo == True:
                return True
    else:
        return False
print(overenie_hesla("Hesl"))



# Úkol 4
"""Napište funkci unikatni_slova, která načte text od uživatele jako řetězec a vypíše počet unikátních slov ve zadaném textu. Program by měl ignorovat velikost písmen, tj. slova "Pes" a "pes" by měla být považována za stejná. (lower, split, set)"""

def unikatni_slova(retezec):
    return set(retezec.lower().split())

text = "ahoj čau nazdar je je je"

print(unikatni_slova(text))

    

    

