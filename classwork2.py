"""Класна робота 2"""
from random import randint
# 11.1
def task_11_1(A):
    A_copy = A.copy()
    minimum = A_copy.pop()

    for i in A:
        if i <= minimum:
            minimum = i

    return minimum

# 11.2
def task_11_2(A):
    A_copy = A.copy()
    while A_copy:
        print(min(A_copy))
        A_copy.remove(min(A_copy))

# 11.3
def task_11_3(univ_set, A):
    return univ_set - A

# 11.4
def task_11_4(A):
    p = 0
    for i in A:
        p += i

    return p

# 11.5
def task_11_5(A):
    a = min(A)
    b = max(A)
    d = abs(a-b)

    return d

# 11.6
def task_11_6():
    seq = {1, 2}
    x_1 = 1
    x_2 = 2

    for x in range(1, 51):
        if x == x_1 + x_2:
            seq.add(x)
            x_1 = x_2
            x_2 = x
        else:
            if x // 10 == 0:
                if x % 10 == 1 or x % 10 == 2:
                    seq.add(x)
            else:
                if x // 10 == 1 or x // 10 == 2:
                    seq.add(x)
    
    for x in seq:
        print(x)

# 11.13
def task_11_13():
    assortment = {'fish', 'meat', 'milk', 'tomatoes', 'apples', 'rice', 'juice'}
    vector = [{x for x in assortment if randint(0, 1) == 1} for _ in range(3)]
    goods_set = vector[0].intersection(assortment)
    in_all_markets = True
    for market in vector[1:]:
        goods_set = market.intersection(goods_set) 
        if not goods_set:
            in_all_markets = False
            break   
    if in_all_markets:
        print(f'{goods_set} - ці товари є у кожному магазині')

    goods_set = set()
    for goods in assortment:
        for market in vector:
            if goods in market:
                goods_set.add(goods)
                break
    if not goods_set:
        print('Немає таких товарів, які були б хоча б в одному магазині')
    else:
        print(f'{goods_set} - кожен з товарів є хоча б в одному з магазинів')

    goods_set = assortment
    for market in vector:
        goods_set.difference_update(market)

    if not goods_set:
        print('Кожен з товарів є хоча б в одному магазині')
    else:
        print(f'{goods_set} - цих товарів немає в жодному з магазинів')
    
    print('\nАсортимент кожного з магазинів: ')
    for m in vector:
        print(m)
    


if __name__ == '__main__':
    A = {1, 3, 4, 6, 2, 5, 7, 8, -1, -3, 3, 54, 1, 3, -1}
    B = {1,10, 11, 12,-5, 3, 4, 6, 2, 5, 7, 8, -1, -3, 3, 54, 1, 3, -1}
    
    print(f'Мінімальний елемент множини: {task_11_1(A)}')

    print('Елементи множини у порядку зростання: ')
    task_11_2(A)

    print(f'Доповнення множини: {task_11_3(B, A)}')

    print(f'Вага числової множини: {task_11_4(A)}')

    print(f'Діаметр числової множини: {task_11_5(A)}')

    task_11_6()

    task_11_13()