class Genre:

    def __init__(self) -> None:
        self.create()

    def create(self, name=None, peculiarities=None):
        self.name = name
        self.peculiarities = peculiarities

    def input(self):
        self.name = input('Name: ')
        self.peculiarities = input('Peculiarities: ').split()

    def output(self):
        print(f'Name: {self.name}')
        print(f'Peculiarities: {self.peculiarities}')

class Carrier:

    def __init__(self) -> None:
        self.create()

    def create(self, carrier_type=None, color=None, storage_duration=None):
        self.carrier_type = carrier_type
        self.color = color
        self.storage_duration = storage_duration

    def input(self):
        self.carrier_type = input('Carrier type: ')
        self.color = input('Color: ')
        self.storage_duration = int(input('Storage duration: '))

    def output(self):
        print(f'Carrier type: {self.carrier_type}')
        print(f'Color: {self.color}')
        print(f'Storage duration: {self.storage_duration}')

class Film(Genre, Carrier):
    def __init__(self) -> None:
        self.create()

    def create(self, author=None, director=None, duration=None):
        Genre().__init__()
        Carrier().__init__()
        self.author = author
        self.director = director
        self.duration = duration

    def input(self):
        Genre.input(self)
        Carrier.input(self)
        self.author = input('Author: ')
        self.director = input('Director: ')
        self.duration = int(input('Duration: '))

    def output(self):
        print("\nInformation about film:")
        Genre.output(self)
        Carrier.output(self)
        print(f'Author: {self.author}')
        print(f'Director: {self.director}')
        print(f'Duration: {self.duration}')
        

if __name__ == '__main__':
    carriers_list = []
    authors_list = []
    directors_list = []
    storage_duration_list = []
    films_list = []
    while True:
        i = input('Add film(a) or quit(q): ')
        if i == 'q':
            break
        elif i != 'a':
            continue
        elif i == 'a':
            f = Film()
            f.input()
            carriers_list.append(f.carrier_type)
            authors_list.append(f.author)
            directors_list.append(f.director)
            storage_duration_list.append(f.storage_duration)
            films_list.append(f)
        
    while True:
        i = input('Show films(show) or quit(q): ')
        if i == 'show':
            j = input('Type of sorting(c - carriers,a - authors, d - directors, s - storage duration)')
            if j == 'c':
                for carrier_type in sorted(carriers_list):
                    for film in films_list:
                        if film.carrier_type == carrier_type:
                            film.output()

            elif j == 'a':
                for author in sorted(authors_list):
                    for film in films_list:
                        if film.author == author:
                            film.output()

            elif j == 'd':
                for director in sorted(directors_list):
                    for film in films_list:
                        if film.director == director:
                            film.output()

            elif j == 's':
                for storage_duration in sorted(storage_duration_list):
                    for film in films_list:
                        if film.storage_duration == storage_duration:
                            film.output()

            else:
                continue

        elif i == 'q':
            break
        else:
            continue

            

