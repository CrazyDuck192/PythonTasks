from time import time
import inspect
from random import shuffle

def timer(func):

    def _timer(*args, **kwargs):
        print(f'Function name: {func.__name__}')
        start = time()
        y = func(*args, **kwargs)
        end = time()
        print(f'Execution time: {end-start}')
        return y
    
    return _timer

def class_timer(cls):
    for name, attr in cls.__dict__.items():
        if not name.startswith('__') and callable(attr):
            setattr(cls, name, timer(attr))
    return cls

@class_timer
class Btree:

    def __init__(self):
        self._data = None
        self._ls = None         
        self._rs = None         

    def isempty(self):
        return self._data == None and self._ls == None and self._rs == None

    def maketree(self, data, t1, t2):
        self._data = data
        self._ls = t1
        self._rs = t2

    def root(self):
        if self.isempty():
            exit(1)
        return self._data

    def leftson(self):
        if self.isempty():
            t = self
        else:
            t = self._ls
        return t

    def rightson(self):
        if self.isempty():
            t = self
        else:
            t = self._rs
        return t

    def updateroot(self, data):
        if self.isempty():
            self._ls = Btree()
            self._rs = Btree()
        self._data = data

    def updateleft(self, t):
        self._ls = t

    def updateright(self, t):
        self._rs = t


if __name__ == '__main__':
    sconst = "apple banana strawberry orange"

    def makewords(s = sconst):
        words = s.split()
        shuffle(words) 
        return words

    def _searchplace(w, t1, t2):
        found = False
        if not t1.isempty():
            if t1.root() == w: 
                found = True
            elif t1.root() > w:
                t1, t2 = t1.leftson(), t1
                found, t1, t2 = _searchplace(w, t1, t2)
            else:
                t1, t2 = t1.rightson(), t1
                found, t1, t2 = _searchplace(w, t1, t2)
        return found, t1, t2
                
    def buildtree(seq):
        t = Btree()
        if len(seq) > 0:
            t.updateroot(seq[0])    
        for w in seq:
            found, t1, t2 = _searchplace(w, t, Btree())
            if not found:
                son = Btree()
                son.updateroot(w)   
                if t2.root() > w:
                    t2.updateleft(son)
                else:
                    t2.updateright(son) 
        return t
                    
    def searchtree(w, t):
        found, t1, t2 = _searchplace(w, t, Btree())
        return found
        
    words = makewords()
    t = buildtree(words)
    print(words)
    while True:
        w = input('Input word: ')
        if len(w) == 0: break
        found = searchtree(w, t)
        print(found)