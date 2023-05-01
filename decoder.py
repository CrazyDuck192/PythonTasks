def prepare_code(message='7 99 19 9 8 65 3 9'):
    mes = message.split()
    pairs = []
    i = 0
    j = 2
    while i != len(mes):
        pairs.append(mes[i:j])
        i, j = j, j+2
    return pairs

def prepare_text(*args):
    symbols = f".,:;-!?'{chr(8212)}{chr(171)}{chr(187)}{chr(8230)}" + '"'
    text_list = []
    for file in args:
        par = 0
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read()
            for symb in symbols:
                while symb in lines:
                    lines = lines.replace(symb, '')
            lines = lines.split('\n\n')
            for par in range(len(lines)):
                lines[par] = lines[par].replace('\n', ' ')
            while True:
                if '' in lines:
                    lines.remove('')
                elif ' ' in lines:
                    lines.remove(' ')
                else:
                    break
        text_list.append(lines)
    return text_list
                

def decoder(pairs, *args):
    cipher = []
    files = prepare_text(*args)
    while True:
        for file in files:
            pair = pairs[0]
            par = file[int(pair[0])-1]
            word = par.split()[int(pair[1])-1]
            cipher.append(word)
            pairs.pop(0)
            if not pairs:
                return ' '.join(cipher)
            

if __name__ == '__main__':
    pairs = prepare_code()
    file1 = 'exercises/books/1.txt'
    file2 = 'exercises/books/2.txt'
    file3 = 'exercises/books/3.txt'
    print(f'Повідомлення: {decoder(pairs, file1, file2, file3)}')
