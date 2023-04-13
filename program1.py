import time

def input_message(method_count=0):
    with open('exercises/2.txt', 'w') as f:
        f.write('')

    with open('exercises/msg.txt', 'a') as f:
        f.seek(0)
        f.truncate()
        while True:
            method = input('Ввести метод та параметри: ')
            if method == 'quit':
                open('exercises/1.txt', 'w').write('quit')
                quit()
            if not method:
                break
            method_count += 1
            string = f'{method}\n'
            f.write(string)

    with open('exercises/1.txt', 'w') as f:
        f.write(str(method_count))

def execution():
    input_message()
    while True:
        try:
            with open('exercises/2.txt', 'r') as f:
                s = f.read()
                if s:
                    break
        except IOError: pass
        time.sleep(1)
    execution()

execution()
