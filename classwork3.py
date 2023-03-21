from math import tan
# Завдання 12.1
print('Завдання 12.1\n')

def calculate(x, filename):
    f = open(filename)
    nums = f.readline().split()
    coef = len(nums) - 1
    s = 0

    for a in nums:
        s += int(a)*x**coef
        coef -= 1
    f.close()

    return s

def diff(n, x, filename):
    f = open(filename)
    nums = f.readline().split()
    coef = len(nums)
    s = 0

    for _ in range(n):
        for i in range(coef):
            coef -= 1
            nums[i] = int(nums[i]) * coef
            if nums[i] == 0:
                del nums[i]
        coef = len(nums)

    coef = len(nums) - 1
    for a in nums:
        s += a*x**coef
        coef -= 1
    f.close()

    return nums, s

filename = 'exercises/classwork3.txt'
s = calculate(3, filename)
print(f'Значення многочлена у точці 3: {s}')

df, s = diff(3, 3, filename)
print(f'Похідна третього порядку: {df}')
print(f'Значення похідної у точці 3: {s}')


# Завдання 12.3
print('\nЗавдання 12.3\n')

def evens(filename):
    f = open(filename)
    nums = f.readline().split()
    answer = []
    for num in nums:
        if int(num) % 2 == 0:
            answer.append(int(num))
    f.close()

    return answer

def squares(filename):
    f = open(filename)
    nums = f.readline().split()
    answer = []
    for num in nums:
        if int(num) > 0:
            if int(num) % 2 != 0 and int(num)**0.5 == int(int(num)**0.5):
                answer.append(int(num))
    f.close()

    return answer

def difference(filename):
    f = open(filename)
    nums = f.readline().split()
    even = []
    odd = []
    for num in nums:
        if int(num) % 2 == 0:
            even.append(int(num))
        else:
            odd.append(int(num))
    f.close()
    
    return max(even) - min(odd)

def sequense(filename):
    f = open(filename)
    nums = f.readline().split()
    length = len(nums)
    seq = []
    answer = 1

    for i in range(length-1):
        seq.append(nums[i])
        j = i
        while True:
            if nums[j+1] <= nums[j]:
                if len(seq) >= answer:
                    answer = len(seq)
                break
            seq.append(nums[j+1])
            j += 1
        seq = []
    f.close()

    return answer

s = evens(filename)
print(f'Усі парні числа: {s}')

s = squares(filename)
print(f'Усі квадрати непарних чисел: {s}')

s = difference(filename)
print(f'Різниця між максимальним парним та мінімальним непарним числами: {s}')

s = sequense(filename)
print(f'Довжина найдовшої зростаючої послідовносі: {s}')

# Завдання 12.4

def array_1(filename, i):
    f = open(filename, 'w')
    f.write(' '.join(str(j) for j in range(1, i+1)))
    f.close()

def array_2(filename, i):
    f = open(filename, 'w')
    f.write(' '.join(str(j**2) for j in range(1, i+1)))
    f.close()

def array_3(filename, i):
    f = open(filename, 'w')
    nums = []

    for j in range(1, i+1):
        num = 1
        while j != 0:
            num *= j
            j -= 1
        nums.append(num)
    f.write(' '.join(str(x) for x in nums))
    f.close()

def array_4(filename, i):
    f = open(filename, 'w')
    f.write(' '.join(str(2**(j+1)) for j in range(1, i+1)))
    f.close()

def array_5(filename, i):
    f = open(filename, 'w')
    f.write(' '.join(str(2**j + 3**(j+1)) for j in range(1, i+1)))
    f.close()

filename = 'exercises/12.4.txt'
array_1(filename, 10)
array_2(filename, 15)
array_3(filename, 8)
array_4(filename, 6)
array_5(filename, 7)

# Завдання 12.5
def func(filename, eps):
    f = open(filename, 'w')
    nums = []
    j = 0
    x = 1

    while True:
        j += 1
        x = (j-0.1)/(j**3 + abs(tan(2*j)))
        if abs(x) < eps:
            break
        nums.append(x)
    for x in nums:
        f.write(f'{str(x)}\n')
    f.close()

func(filename, 0.001)