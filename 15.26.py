class HyperString:

    def __init__(self):
        self.syms = []
        self.delim = ' '

    def console_input(self):
        while True:
            sym = str(input('Ввести рядок: '))
            if sym == '':
                break
            self.syms.append(sym)

    def console_output(self):
        print(self.delim.join(self.syms))

    def file_input(self, filename):
        try:
            with open(filename, 'r') as f:
                s = f.read()
                if self.delim != ' ':
                    s = s.replace(' ', self.delim)
                self.syms = s.split(self.delim)
        except FileNotFoundError:
            print('Файл не знайдено!')
        else:
            return s
        
    def file_output(self, filename):
        with open(filename, 'w') as f:
            f.write(' '.join(self.syms))

    def input_delim(self, delim):
        self.delim = delim

    def concatenation(self):
        return self.delim.join(self.syms)
    
    def length(self):
        return len(self.syms)
    
    def merger(self, sym_list):
        self.syms.append(''.join(sym_list))
    
    def __getitem__(self, key):
        try:
            return self.syms[key]
        except IndexError:
            print('Елемента з таким індексом не існує!')  
    
    def delete(self, key):
        try:
            del self.syms[key]  
        except IndexError:
            print('Елемента з таким індексом не існує!')  


if __name__ == '__main__':    
    s = HyperString()
    s.input_delim('---')
    s.file_input('exercises/15.26.txt')
    s.console_output()
    s.merger(['abc', 'qqq', 'wer'])
    s.console_output()
    s.file_output('exercises/task_15_26.txt')
