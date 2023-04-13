import time

def execution_cls(cls):
        error_number = 0
        execution_number = 0
        with open('exercises/1.txt', 'r+') as f:
            if f.readline().split()[0] == 'quit':
                f.truncate(0)
                quit()    
            f.truncate(0)

        with open('exercises/msg.txt') as f:
            lines = f.readlines()
            for line in lines:
                line = line.split()
                if line[0] == 'quit':
                    quit()
                elif line[0] == 'call':
                    print(f'Виконання методу {line[1]}:')
                    try:
                        method = getattr(cls, line[1])
                        method(cls, *line[2:])
                        execution_number += 1
                    except AttributeError:
                        error_number += 1
                        print(f'  Методу {line[1]} немає у класі!')
                    except TypeError:
                        error_number += 1
                        print('  Некоректна кількість параметрів: метод не виконано!')
                elif line[0] == 'add_method':
                    print(f'Додавання методу {line[1]}:')
                    length = int(line[2])
                    def dynamic_method(self, *args):
                        if len(args) == length:
                            print(*args)
                        else:
                            raise TypeError
                    setattr(cls, line[1], dynamic_method)
                    print(f'  Метод {line[1]} додано!')
                    execution_number += 1
        print(f'Виконано: {execution_number}; помилок: {error_number}.')

        with open('exercises/2.txt', 'w') as f:
            f.write(str(execution_number+error_number))

class Recepient:

    def __init__(self):
        pass

    def method_1(self, a):
        print(a)
    
    def method_2(self, a, b, c):
        print(a, b, c)

def execution_main():
    while True:
        try:
            with open('exercises/1.txt', 'r') as f:
                s = f.read()
                if s:
                    break
        except IOError: pass
        time.sleep(1)

    execution_cls(Recepient)
    execution_main()


execution_main()