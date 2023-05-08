from random import shuffle

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

class TraceMixin(object):

    def __getattribute__(self, method):
        print(f'Name of attribute: {method}')
        return object.__getattribute__(self, method)
    
class TracedBtree(Btree, TraceMixin):
    pass

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
        t = TracedBtree()
        if len(seq) > 0:
            t.updateroot(seq[0])    
        for w in seq:
            found, t1, t2 = _searchplace(w, t, TracedBtree())
            if not found:
                son = TracedBtree()
                son.updateroot(w)   
                if t2.root() > w:
                    t2.updateleft(son)
                else:
                    t2.updateright(son) 
        return t
                    
    def searchtree(w, t):
        found, t1, t2 = _searchplace(w, t, TracedBtree())
        return found
       
    words = makewords()
    t = buildtree(words)
    print(words)
    while True:
        w = input('Input word: ')
        if len(w) == 0: break
        found = searchtree(w, t)
        print(found)