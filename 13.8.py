class MultiSet:

    def __init__(self):

        self.dct = {}

    def makeEmpty(self):
        self.dct.clear()

    def isEmpty(self):
        return not bool(self.dct)

    def addElement(self, el):
        self.dct[el] = self.dct.get(el, 0) + 1

    def popElement(self, el):
        self.dct[el] = self.dct.get(el, 0) - 1
        if self.dct[el] <= 0:
            del self.dct[el]

    def countElement(self, el):
        return self.dct.get(el, 0)

    def union(self, ms):
        
        keys1 = set(self.dct.keys())
        keys2 = set(ms.dct.keys())

        keys = keys1 | keys2

        for item in keys:
            self.dct[item] = max(self.dct.get(item, 0), ms.dct.get(item, 0))

    def intersect(self, ms):

        keys1 = set(self.dct.keys())
        keys2 = set(ms.dct.keys())

        keys = keys1 & keys2

        rem = keys1 - keys2
        for item in rem:
            del self.dct[item]

        for item in keys:
            self.dct[item] = min(self.dct.get(item, 0), ms.dct.get(item, 0)) 

    def __str__(self):
        st = "{"
        for k, v in self.dct.items():
            st += f"({k}, {v}), "
        st += "}\n"
        return st

if __name__ == "__main__":

    m1 = MultiSet()
    m1.addElement(3)
    m1.addElement(2)
    m1.addElement(1)
    m1.addElement(3)
    m1.addElement(3)
    m1.addElement(1)
    print(m1)

    m2 = MultiSet()
    m2.addElement(1)
    m2.addElement(3)
    m2.addElement(1)
    m2.addElement(3)
    m2.addElement(3)
    m2.addElement(1)
    print(m2)

    m1.union(m2)
    print(m1)

    m1.intersect(m2)
    print(m1)

