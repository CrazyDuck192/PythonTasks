class Segment:

    def __init__(self, a, b):
        assert a <= b, 'b > a'
        self.a = a
        self.b = b

        if self.a == self.b:
            self.empty = True
        else:
            self.empty = False
        
        self.seg = (self.a, self.b, self.empty)

    def __str__(self):
        return f'({self.a}, {self.b}, {self.empty})'

    def make_empty(self):
        self.a = self.b = 0
        self.empty = True

    def is_empty(self):
        return self.empty
    
    def intersect(self, t):
        if self.empty or t.empty:
            return self.make_empty()

        if self.b < t.a or self.a > t.b:
            return self.make_empty()

        if self.a >= t.a and self.b <= t.b:
            return self
        elif self.a <= t.a and self.b >= t.b:
            return t
        
        if self.a >= t.a and self.b >= t.b:
            return Segment(self.a, t.b)
        elif self.a <= t.a and self.b <= t.b:
            return Segment(t.a, self.b)
    


    

if __name__ == "__main__":
    # t1 = Segment(-1, 3)
    # t2 = Segment(0, 9)
    # t = t1.intersect(t2)
    # print(t)

    p = int(input('p = '))
    q = int(input('q = '))
    d = p**2 - 4*q
    x_1 = (-p - d**0.5)/2
    x_2 = (-p + d**0.5)/2
    t_1 = Segment(x_1, x_2)

    p = int(input('p = '))
    q = int(input('q = '))
    d = p**2 - 4*q
    x_1 = (-p - d**0.5)/2
    x_2 = (-p + d**0.5)/2
    t_2 = Segment(x_1, x_2)

    print(t_1.intersect(t_2))


