class Person: #Клас Особа
    def __init__(self, name = '', surname = '', age = 0):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'{self.name} {self.surname}, {self.age}'

    def input(self):
        self.name = input('Enter name: ')
        self.surname = input('Enter surname: ')
        self.age = int(input('Enter age: '))

    def __repr__(self):
        return f'Person({self.name}, {self.surname}, {self.age})'

class Acquainted(Person):
    def __init__(self, name = '', surname = '', age = 0, phone_numb = ''):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_numb = phone_numb

    def __str__(self):
        return f'{self.name} {self.surname} {self.age} {self.phone_numb}'

    def inp_phone(self):
        self.phone_numb = input('Enter phone number: ')

    def set_phone(self, phone_numb):
        self.phone_numb = phone_numb

    def get_phone(self):
        return self.phone_numb

class Notebook:
    def __init__(self, fname):
        self.lst = []
        self.fname = fname
        try:
            f = open(fname)
            for line in f.readlines():
                s1 = line.split()[0]
                s2 = line.split()[1]
                s3 = int(line.split()[2])
                s4 = line.split()[3]
                acq = Acquainted(s1, s2, s3, s4)
                self.lst.append(acq)
            f.close()
        except:
            print('Bad file')

    def upd(self, a = None):
        if a is None:
            a = Acquainted()
            a.input()
            a.inp_phone()
        self.lst.append(a)
        f = open(self.fname, 'w+')
        for x in self.lst:
            f.write(' '.join([x.name, x.surname, str(x.age), x.phone_numb]))
            f.write('\n')
        f.close()

    def upd2(self):
        n = int(input('Number of acquaintance: '))
        for _ in range(n):
            self.upd()
        f = open(self.fname, 'w+')
        for x in self.lst:
            f.write(' '.join([x.name, x.surname, str(x.age), x.phone_numb]))
            f.write('\n')
        f.close()

    def __str__(self):
        return '\n'.join(str(x) for x in self.lst)

    def finder(self, surname):
        for item in self.lst:
            if item.surname == surname:
                return item.get_phone()
        return None

    def changer(self, surname, new_phone):
        for item in self.lst:
            if item.surname == surname:
                item.set_phone(new_phone)
                return True
        return None


if __name__ == "__main__":
    p = Person()
    p.input()
    print(p)
    print(repr(p))
    a = Acquainted()
    a.input()
    a.inp_phone()
    print(a)

