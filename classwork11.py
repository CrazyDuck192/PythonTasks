# Завдання 16.1
class Iterator_1:

    def __init__(self, n, multiplicity):
        self.n = n 
        self.k = 0
        self.multiplicity = multiplicity

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.k + 2 > self.n:
            raise StopIteration
        if self.multiplicity == 'even':
            self.k += 2
            return self.k
        elif self.multiplicity == 'odd':
            self.k += 1
            if self.k % 2 != 0:
                return self.k 
            else:
                self.k += 1
                return self.k

# Завдання 16.2            
class Iterator_2:

    def __init__(self, n, multiplicity):
        self.n = n + 1
        self.multiplicity = multiplicity

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= 2:
            raise StopIteration
        if self.multiplicity == 'even':
            if self.n % 2 == 0:
                self.n -= 2
                return self.n 
            else:
                self.n -= 1
                return self.n
        elif self.multiplicity == 'odd':
            if self.n % 2 != 0:
                self.n -= 2
                return self.n 
            else:
                self.n -= 1
                return self.n
            
# Завдання 16.3
class Iterator_3:

    def __init__(self, sequence, multiplicity):
        self.sequence = sequence
        self.multiplicity = multiplicity
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        if self.multiplicity == 'even':
            element = self.sequence[self.index]
            self.index += 2
            return element
        elif self.multiplicity == 'odd':
            if self.index == 0:
                self.index += 1
            element = self.sequence[self.index]
            self.index += 2
            return element
        
# Завдання 16.4
class Iterator_4:

    def __init__(self, sequence, multiplicity):
        self.sequence = sequence
        self.multiplicity = multiplicity
        self.index = len(self.sequence) - 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        if self.multiplicity == 'even':
            if self.index % 2 != 0:
                self.index -= 1
            element = self.sequence[self.index]
            self.index -= 2
            return element
        elif self.multiplicity == 'odd':
            if self.index % 2 == 0:
                self.index -= 1
            element = self.sequence[self.index]
            self.index -= 2
            return element


if __name__ == '__main__':
    i_1 = Iterator_1(11, 'odd')
    for x in i_1:
        print(x)

    i_2 = Iterator_2(11, 'even')
    for x in i_2:
        print(x)

    i_3 = Iterator_3('abcdefgh', 'odd')
    for x in i_3:
        print(x)

    i_4 = Iterator_4('abcdefgh', 'even')
    for x in i_4:
        print(x)
