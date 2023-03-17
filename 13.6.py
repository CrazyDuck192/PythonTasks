from collections import defaultdict

class Polynom:
    
    def __init__(self):
        self.poly = defaultdict(int)

    def input(self):
        self.degree = int(input('Степінь полінома: '))
        for i in range(self.degree, -1, -1):
            coef = int(input(f'Коефіцієнт при x^{i}: '))
            self.poly[i] = coef

    def __str__(self):
        terms = [f'{a}*x^{b}' for b, a in reversed(sorted(self.poly.items())) if a != 0]
        return ' + '.join(terms)       

    def calculate(self, x):
        return sum([coef*x**degree for degree, coef in self.poly.items()])

    def derivative(self, der_degree):
        for _ in range(der_degree):
            for degree in range(self.degree+1):
                self.poly[degree-1] = self.poly.pop(degree) * degree
            self.degree -= 1

    def __add__(self, other):
        p3 = Polynom()
        p3.poly = self.poly
        for degree in other.poly.keys():
            p3.poly[degree] = self.poly[degree] + other.poly[degree]
        return p3

    def __sub__(self, other):
        p3 = Polynom()
        p3.poly = self.poly
        for degree in other.poly.keys():
                p3.poly[degree] = self.poly[degree] - other.poly[degree]

        return p3

    def __mul__(self, other):
        p3 = Polynom()
        for i in range(len(self.poly), -1, -1):
            for j in range(len(other.poly), -1, -1):
                if i+j not in p3.poly.keys():
                    p3.poly[i+j] = self.poly[i] * other.poly[j]
                else:
                    p3.poly[i+j] += self.poly[i] * other.poly[j]

        return p3

if __name__ == "__main__":
    p1 = Polynom()
    p1.input()
    print(p1.calculate(4))

    