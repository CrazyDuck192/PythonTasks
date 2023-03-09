class Iterator:

    def __init__(self, data, indicator):
        self.data = data.copy()
        self.indicator = indicator
        

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indicator == 'increase':
            if not self.data:
                raise StopIteration
            el = min(self.data)
            self.data.remove(el)
            return el
        elif self.indicator == 'decrease':
            if not self.data:
                raise StopIteration
            el = max(self.data)
            self.data.remove(el)
            return el
        
if __name__ == '__main__':
    seq = [4, 7, 1, 8, 2, 3, 4, 0, 9]
    seq_iter = Iterator(seq, 'increase')
    for i in seq_iter:
        print(i)

    seq_iter = Iterator(seq, 'decrease')
    for i in seq_iter:
        print(i)

