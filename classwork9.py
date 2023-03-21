# Завдання 15.1
def getValue(s, d):

    assert 2 <= d <= 16, f'{d} is not in 2..16'

    digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    digit_val = [i for i in range(16)]

    result = 0
    for c in s:
        if c.lower() not in digits:
            print('stop!')
            assert False, f'{c} is not correct digit for d = {d}'
            return None    
        index = digits.index(c)

        if index >= d:
            print('stop!')
            assert False, f'{c} is not correct digit for d = {d}'
            return None 

        digit = digit_val[index]

        result = result*d + digit
        print('b = ', index,'n = ', result)

    return result

# Завдання 15.2
def ln(x, eps):
    assert abs(x) < 1, f'|x| < 1'
    assert eps >= 0, 'epsilon should be positive'
    y = 0
    k = 0
    while True:
        y0 = y
        y += (-1)**k * x**(k+1) / (k+1)
        k += 1
        if abs(y - y0) <= eps:
            break
    return y

# Завдання 15.4
def sum(*x, **y):
    assert len(x) == len(y.keys()), f'size x not equal size y'
    s = 0
    for a,b in enumerate(y.keys()):
        s += x[a]**2 + y[b]**2 + x[a]*y[b]
    return s

# Завдання 15.5
def numbers_file(n, filename_1, filename_2):
    try:
        with open(filename_1) as f:
            g = open(filename_2, 'w')
            numbers = f.readline().split()
            n_0, k = 0, n

            while n < len(numbers):
                g.write(f"{max(map(int, numbers[n_0:n]))} ")
                n_0, n = n_0+k, n+k           
            g.write(f"{max(map(int, numbers[n_0:]))} ")
            g.close()
            
    except FileNotFoundError:
        print(f'File {filename_1} not found')


if __name__ == "__main__":
    # 15.1
    print(getValue('101', 2))
    print(getValue('102', 3))

    print(getValue('abc', 16))
    print(getValue('819', 10))

    s = input('Input number: ')

    d = int(input('d = '))

    n = getValue(s, d)

    print('n = ', n)

    # 15.2
    y = ln(-0.5, 0.0001)
    print(y)

    y = ln(1, 0.0001)
    print(y)

    # 15.4
    s = sum(2, 3, 4, y1 = 5, y2 = 6, y3 = 7)
    print(s)
    
    s = sum(2, 3, y1 = 5, y2 = 6, y3 = 7)
    print(s)

    # 15.5
    f = 'exercises/15.5_f.txt'
    g = 'exercises/15.5_g.txt'
    numbers_file(5, f, g)