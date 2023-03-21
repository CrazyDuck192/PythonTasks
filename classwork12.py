from math import factorial
# Завдання 16.16(а, б)

def task_a(k, x, eps):
    assert k >= 0, "Число k повинно бути невід'ємним"
    for d in range(k+1):
        yield (-1)**d * x**(2*d+1)/factorial(2*d+1)

    k = 0
    s = 0
    y = 1
    while abs(y) >= eps:
        y = (-1)**k * x**(2*k+1)/factorial(2*k+1)
        s += y
        k += 1
    yield f'Sum = {s}'

def task_b(k, x, eps):
    assert k >= 0, "Число k повинно бути невід'ємним"
    for d in range(k+1):
        yield x**(2*d)/factorial(2*d)

    k = 0
    s = 0
    y = 1
    while abs(y) >= eps:
        y = x**(2*k)/factorial(2*k)
        s += y
        k += 1
    yield f'Sum = {s}'

# Завдання 16.17(а)

def log(x, eps):
    assert abs(x) < 1, '|x| < 1'
    y = 1
    k = 1
    while abs(y)>0:
        y = (-1)**(k+1)*x**k/k
        k += 1
        yield y

    k = 1
    ln = 0
    y = 1
    while abs(y) >= eps:
        y = (-1)**(k+1)*x**k/k
        ln += y
        k += 1

    yield f'log({1+x}) = {ln}'

if __name__ == '__main__':
    seq = task_a(10, 10, 0.001)
    for x in seq:
        print(x)

    seq = task_b(20, 5, 0.0001)
    for x in seq:
        print(x)

    ln = log(0.5, 0.00001)
    for x in ln:
        print(x)