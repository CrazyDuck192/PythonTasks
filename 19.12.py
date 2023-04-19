import json
import random

word = ""
guessed = ""

class RlistMeta(type):
    def __init__(cls, name, bases, nmspc):
        super().__init__(name, bases, nmspc)
        def save(self, filename):
            global word, guessed
            with open(filename, 'w') as f:
                number = 1
                dct = {}
                players = {}
                for x in self._lst:
                    players[f'Player {number}'] = {
                        '__class__': x.__class__.__name__,
                        'points': x._points,
                        'name': x._name
                    }
                    number += 1
                dct['_lst'] = players
                dct['_cur'] = self.__dict__['_cur']
                dct['word'] = word
                dct['guessed'] = guessed
                json.dump(dct, f, indent=4)

        def load(self, filename):
            with open(filename, 'r+') as f:
                global word, guessed
                data = json.load(f)
                for player in data['_lst'].values():
                    print(player)
                    class_name = player.pop('__class__')
                    get_class = globals()[class_name]
                    self._lst.append(get_class(**player))
                self._cur = data['_cur']
                word = data['word']
                guessed = data['guessed']

        cls.save = save
        cls.load = load

class Rlist(metaclass=RlistMeta):

    def __init__(self):
        self._lst = []                  
        self._cur = None                

    def len(self):
        return len(self._lst)

    def next(self):
        l = self.len()
        if l != 0:
            if self._cur == l-1:
                self._cur = 0
            else:
                self._cur += 1

    def getcurrent(self):
        if self.len() == 0:
            exit(1)
        data = self._lst[self._cur]
        return data

    def update(self, data):
        if self.len() == 0:
            exit(1)
        self._lst[self._cur] = data

    def insert(self, data):
        if self.len() == 0:       
            self._lst.append(data)
            self._cur = 0
        else:
            self._lst.insert(self._cur,data)
            self._cur += 1           

    def delete(self):
        if self.len() == 0:
            exit(1)
        l = self.len()
        del self._lst[self._cur]
        if l == 1:                 
            self._cur = None
        elif self._cur == l-1:      
            self._cur = 0                        
                                                            
    def __del__(self):
        del self._lst

class Guesser:
    def __init__(self, name, points=0):
        self._name = name          
        self._points = points          

    def show(self):
        print(self._name, self._points)

    def inc(self, points):
        self._points += points

    def clear(self):
        self._points = 0

    def getname(self):
        return self._name

def makeword():
    global word, guessed
    word = random.choice(['apple', 'banana', 'orange', 'carrot', 'pumpkin', 'watermelon'])
    guessed = "*"*len(word)
    return word, guessed

def inputguessers(guessers):
    while True:
        name = input("Ім'я гравця: ")
        if len(name) == 0: break
        g = Guesser(name)           
        guessers.insert(g)

def guess():
    global word, guessed, gameover
    while True:
        m = input("1 - вказати літеру, 2 - вказати слово: ")
        if m in {"1", "2"}: break
    if m == '1':                          
        while True:
            c = input('Літера: ')
            if not c in guessed: break
            print(c,' - ця літера вже вгадана!')
        points = 0
        gw = ""
        for i in range(len(word)):
            if word[i] == c:
                gw = gw + c        
                points += 1         
            else:
                gw = gw + guessed[i]
        guessed = gw
    else:                           
        w = input('Слово: ')
        if w == word:              
            points = guessed.count('*') 
            guessed = word
        else:                       
            points = -1             
    gameover = not '*' in guessed   
    return points

def play(guessers):
    global guessed, gameover
    gameover = False
    while not gameover:
        while True:
            guessers.save(file)
            print(guessed)        
            g = guessers.getcurrent()
            print(g._name)
            print('Ваш хід,', g.getname())
            points = guess()
            if points > 0:
                g.inc(points)
                print('Ваші бали:', points)
                if gameover:
                    g.inc(len(word)) 
                    print(f'Переможець!!!')
                    g.show()
            elif points < 0:
                print('Ваші бали "згоріли"')
                g.clear()
            if gameover or points <= 0: break 
        guessers.next()          
    print('Вгадане слово - ', word)         

if __name__ == '__main__':
    is_load = int(input('Почати нову гру чи завантажити дані старої гри? (1 - нова гра, 2 - завантажити стару): '))
    file = 'exercises/guesser_game.json'
    guessers = Rlist()
    if is_load == 1:
        makeword()
        inputguessers(guessers)
        play(guessers)
    else:
        guessers.load(file)
        play(guessers)