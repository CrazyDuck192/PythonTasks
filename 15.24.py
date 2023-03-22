
class IncorrectData(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f'{self.n} is incorrect'

class FileProblem(Exception):

    def __init__(self, fname, msg):
        self.fname = fname
        self.msg = msg

    def __str__(self):
        return f'{self.fname} is not open: {self.msg}'

class WorkBinFile:

    def __init__(self, fname):
        self.fname = fname
        self.num = 0

    def input_console(self):

        n = int(input('n = '))

        if n <= 0:
            raise IncorrectData(n)
        
        f = open(self.fname, 'wb')
        if not f:
            raise FileProblem(self.fname, 'cannot open')
        for _ in range(n):
            x = int(input('x = '))
            f.write(x)

        f.close()

    def write_from_list(self, lst):

        f = open(self.fname, 'wb')
        if not f:
            raise FileProblem(self.fname, 'cannot open')
        for x in lst:
            f.write(bytearray([x]))

        f.close()

    def read(self):

        f = open(self.fname, 'rb')
        if not f:
            raise FileProblem(f, 'cannot read')
        while True:
            x = f.read(1)
            x = int.from_bytes(x, byteorder='big')
            print(x)
            if not x:
                break

        f.close()

    def append(self, data):

        f = open(self.fname, 'a+b')
        if not f:
            raise FileProblem(self.fname, 'cannot append')
        f.write(bytearray(data))
        f.close()

if __name__ == "__main__":
    try:
        wf = WorkBinFile('1.dat')
        wf.write_from_list([1, 2, 3, 4, 7, 4, 8, 9])
        wf.append(8)
        wf.read()
    
    except FileProblem as e:
        print(e)
