## 2. bodovaný úkol
### Analýza geografických dat

Získání dat:
Vyberte si nějaká geografická data, která vás zajímají. Může to být například dataset s polohami míst, teplotami, nebo něco spojené s geografickými informacemi. Data můžete načíst ze souboru (například txt, CSV, GeoJSON)

Zpracování dat:
Zpracujte a analyzujte data v Pythonu. Vypočtěte základní statistiky o geografických datech (průměrná délka, plocha, atd.). Identifikujte a vizualizujte největší nebo nejmenší hodnoty v datech. Například můžete provést agregaci dat, filtrování nebo jiné transformace. Uložte transformovaná nebo analyzovaná data do nového souboru.

Vizualizace dat:
Data vhodným způsobem vizualizujte. Můžete použít knihovny pro tvorbu grafů (např. Matplotlib, Plotly), nastudujte si jejich použití.

Dokumentace:
Kód důkladně okomentujte a vytvořte krátký dokumentační soubor, kde popíšete, jakým způsobem jste získali data, jak jste je zpracovali a jak se používá váš skript.


# Objektově orientované programování (OOP)
Objektové orientované programování má celou řadu výhod oproti klasickému deklarativnímu paradigmatu. Pro větší projekty umožňuje znovupoužitelnost kódu, zaručuje větší modularitu a přehlednost kódu a při správném použití dokáže zjednodušit celý návrh.
Výhody OOP:
 * rychlejší a levnější vývoj větších aplikací
 * lepší udržitelnost kódu

Nevýhody OOP:
 * lehce komplikovaný pro začátečníky
 * výpočetně může být tento přístup o něco málo pomalejší

Pro použití objektově orientovaného programování potřebujeme používat jazyk, který toto paradigma podporuje. Mezi takové jazyky patří například Java, C++, Python, C#, Swift nebo Scala. Naopak mezi jazyky, které OOP nepodporují, patří C, Haskell, Fortran nebo Pascal.

## Proč OOP?

Představme si, že máme za úkol vytvořit systém pro správu informací o knihách v knihovně. Chceme evidovat názvy knih, autory a počet dostupných kopií. Zvažme různé způsoby, jak tato data uložit.

Můžeme začít vytvořením seznamu pro každou knihu, kde budeme ukládat název knihy, autora a počet dostupných kopií.

```python
book_1 = ["Pán Prstenů", "J.R.R. Tolkien", 10]
book_2 = ["Harry Potter", "J.K. Rowling", 8]
```

Na první pohled mohou kolegové považovat poslední hodnotu za hodnocení knihy. Abychom tomu předešli, můžeme přidat komentáře, ale ani to není ideální řešení.

Další možností je použití slovníku, kde budeme ukládat informace o každé knize ve formě klíč-hodnota.

```python
book_1 = {"title": "Pán Prstenů", "author": "J.R.R. Tolkien", "copies_available": 10}
book_2 = {"title": "Harry Potter", "author": "J.K. Rowling", "copies_available": 8}
```

Nyní můžeme přemýšlet o tom, jak bychom řešili situaci, kdy čtenář chce vypůjčit knihu. Podobně jako v předchozím příkladu, snížíme počet dostupných kopií, ale musíme zkontrolovat, zda čtenář nemůže půjčit více kopií, než kolik jich je k dispozici.

```python
def borrow_book(copies_to_borrow, book):
    if copies_to_borrow <= book["copies_available"]:
        book["copies_available"] -= copies_to_borrow
        print("Kniha půjčena.")
    else:
        print("Omlouváme se, nemáme dostatek kopií k vypůjčení.")

borrow_book(5, book_1)
# Vypíše Kniha půjčena.

```

Toto řešení může být rozsáhlejší a obtížněji udržovatelné, pokud máme více funkcí a knih v našem systému. Pro eliminaci těchto problémů můžeme využít objektově orientované programování (OOP).

V OOP můžeme vytvořit třídu, která reprezentuje knihu a obsahuje atributy (název, autor, dostupné kopie) a metody (např. půjčení knihy). Každá kniha v našem systému bude instancí této třídy, což zjednoduší přidávání nových knih a zajiští jednotné rozhraní pro práci s knihami v celém programu.


## Objekty a třídy
Objekty a třídy jsou základem objektově orientovaného programování (OOP), které využívá třídy a instance (objekty).

Objekty slouží k reprezentaci entit v reálném světě, jako například zaměstnanci ve firmě. Na rozdíl od slovníků umožňují objekty propojit data o zaměstnancích s kódem, který zpracovává tato data.

Vytvoření třídy je prvním krokem. Můžeme si představit třídu jako prázdný formulář, který obsahuje kolonky, které by měly být vyplněny. Objekt pak představuje vyplněný formulář s konkrétními daty.

Podobně jako vyplňujeme více formulářů na základě jednoho formuláře, může vzniknout několik objektů na základě jedné třídy. Objekty jsou nezávislé, takže změny v jednom objektu neovlivňují ostatní. Tento princip se nazývá zapouzdření.

Třídy mají atributy (uchovávají hodnoty) a metody (vykonávají příkazy). Atributy jsou podobné hodnotám ve slovníku, a metody jsou obdobou funkcí. Každá metoda pracuje s daty konkrétního objektu.

Začneme tím, že vytvoříme třídu Employee, která reprezentuje zaměstnance. Třída bude mít atributy jméno, pracovní pozici a nárok na dovolenou. Poté vytvoříme speciální metodu init(), která se stará o vytvoření objektu a nastavení hodnot jeho atributů.

```python
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    
    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
```

Nyní můžeme vytvořit objekty zaměstnanců a pracovat s nimi pomocí definovaných metod.

```python
frantisek = Employee("František Novák", "konstruktér", 25)
print(frantisek.get_info())

klara = Employee("Klára Nová", "konstruktérka", 25)
print(klara.get_info())
```

Díky použití třídy a objektů můžeme jednoduše vytvářet a spravovat zaměstnance, a to včetně jejich individuálních informací. Každý objekt obsahuje své vlastní hodnoty atributů, což zajišťuje oddělenost dat mezi jednotlivými zaměstnanci.

Objektově orientované programování nám tak umožňuje vytvářet struktury, které lépe modelují reálný svět a usnadňují správu a manipulaci s daty.

Nyní se zaměříme na problematiku čerpání dovolené a  obohatíme naši třídu o novou metodu - take_holiday(). Tato metoda bude hlídat, aby zaměstnanec/zaměstnankyně nepřečerpal(a) svůj nárok na dovolenou.

```python
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."
```

Nyní můžeme vidět, jak budou vyřizovány Františkovy žádosti o dovolenou.

```python
frantisek = Employee("František Novák", "konstruktér", 25)

print(frantisek.take_holiday(5))
print(frantisek.take_holiday(15))
print(frantisek.take_holiday(10))
```

Dále jsme se pokusili zjednodušit použití naší třídy. I když třída umí přehledně vypsat informace díky metodě get_info(), může se stát, že někdo, kdo ji používá, si této metody nevšimne a intuitivně vyzkouší funkci print().

```python
print(frantisek)
```

Odpovědí byl záhadný text ve stylu <__main__.Employee object at 0x00000126F0084850>. Funke print() se pokusí převést objekt na typ řetězec, a protože naše třída nemá tuto funkci naprogramovanou, použije se standardní formát. Místo toho by bylo užitečnější získat informaci, jak ji máme připravenou v metodě get_info().

Převod na řetězec zařídíme přidáním metody __str__. Tato metoda bude použita vždy, když Python bude chtít převést objekt na řetězec. Můžeme tedy přejmenovat metodu get_info() na __str__.

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

frantisek = Employee("František Novák", "konstruktér", 25)
print(frantisek)
```

Tím jsme ukázali, jak vytvořit třídu, objekty a jak s nimi pracovat, a zároveň jsme implementovali čerpání dovolené pomocí nové metody.

