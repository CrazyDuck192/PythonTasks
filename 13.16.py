from collections import defaultdict

class SparceMatrix:

    def __init__(self):
        self.matrix = defaultdict(int)

    def input(self):
        self.size = input('Розміри матриці: ').split()
        

    
m = SparceMatrix()
m.input()