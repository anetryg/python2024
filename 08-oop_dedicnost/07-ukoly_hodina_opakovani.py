# Úkol 1
""" Vytvořte třídu Car, která reprezentuje automobil. Třída by měla mít atributy brand (značka auta), model (model auta), a is_running (informace o tom, zda je auto zapnuté - True, pokud ano, False, pokud ne). Přidej metodu start_engine(), která zapne motor auta, pokud není již zapnutý.
"""

class Car:
    def __init__(self, brand, model, is_running):
        self.brand = brand
        self.model = model
        self.is_running = is_running

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"Motor auta {self.brand} {self.model} byl zapnut.")
        else:
            print(f"Motor auta {self.brand} {self.model} už běží.")

car = Car("Škoda", "Octavia, False")
car.start_engine()
car.start_engine()




# Úkol 2
""" Navrhněte třídu Movie reprezentující film. Třída by měla mít atributy title (název filmu), director (režisér), a duration (délka filmu v minutách). Přidej metodu get_full_info(), která vypíše kompletní informace o filmu. Pokud je délka filmu neznámá (None), vypište pouze název a režiséra.
"""

class Movie:
    def __init__(self, title, director, duration=None):
        self.title = title
        self.director = director
        self.duration = duration

    def get_full_info(self):
        if self.duration is None:
            return f"Film: {self.title}, Režisér: {self.director}"
        else:
            return f"Film: {self.title}, Režisér: {self.director}, Délka: {self.duration} minut"


movie = Movie("Pulp Fiction", "Quentin Tarantino", 154)
print(movie.get_full_info())



# Úkol 3
""" Vytvoř třídu Song reprezentující píseň. Třída by měla mít atributy title (název písně), artist (interpret), duration (délka písně v minutách), a genre (žánr písně, defaultně nastaven na "Pop"). Přidej metodu play(), která vypíše zprávu o přehrávání písně. Před přehráním písně ověřte, zda je délka písně větší než 0, a vypište odpovídající zprávu.
"""

class Song:
    def __init__(self, title, artist, duration, genre="Pop"):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def play(self):
        if self.duration > 0:
            print(f"Přehrává se píseň '{self.title}' od {self.artist}.")
        else:
            print(f"Píseň '{self.title}' nelze přehrát, protože nemá platnou délku.")

song = Song("Bohemian Rhapsody", "Queen", 0)
song.play()


# Úkol 4
""" Vytvořte třídu Dog reprezentující psa. Třída by měla mít atributy name (jméno psa), breed (plemeno psa), age (věk psa), a is_hungry (informace o tom, zda je pes hladový - True, pokud ano, False, pokud ne). Přidej metodu feed(), která nakrmí psa a změní stav is_hungry na False. Pokud je pes již nakrmený, vypište o tom informaci.
"""

class Dog:
    def __init__(self, name, breed, age, is_hungry):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_hungry = is_hungry

    def feed(self):
        if self.is_hungry:
            self.is_hungry = False
            print(f"{self.name} byl nakrmen a už není hladový.")
        else:
            print(f"{self.name} už je nakrmený a nemá hlad.")


dog = Dog("Abby", "Golden Retriever", 3, True)
dog.feed()
dog.feed()