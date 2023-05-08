import json

class Person:
    def __init__(self):
        self.surname = None
        self.byear = None

    def input(self):
        self.surname = input('Прізвище: ')
        self.byear = input('Рік народження: ')

    def print(self):
        print(f'Прізвище: {self.surname}')
        print(f'Рік народження: {self.byear}')

class Student(Person):

    def __init__(self, filename):
        Person().__init__()
        self.name = None
        self.course = None
        self.marks = {}
        self.file = filename
    
    def input(self):
        Person.input(self)
        self.name = input("Ім'я: ")
        self.course = input('Курс: ')
        n = int(input('Кількість предметів: '))
        for _ in range(n):
            subject = input('Предмет: ')
            mark = input('Оцінка з предмета за сесію: ')
            self.marks[subject] = mark

    def print(self):
        Person.print(self)
        print(f"Ім'я: {self.name}")
        print(f'Курс: {self.course}')
        for k, v in self.marks.items():
            print(f'{k}: {v}')
        
    def save(self, data):
        with open(self.file, 'r+') as f:
            data_json = json.load(f)
            data_json.append(data)
            f.seek(0)
            json.dump(data_json, f, indent=4)

if __name__ == '__main__':
    p = Student()
    p.input()
    p.print()

    