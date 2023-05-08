from task_14_3 import Queue
from random import randint

stack = Queue()
m = int(input('m = '))
for i in range(1, m+1):
    stack.push(i)

n = int(input('Кількість випробувань: '))
for _ in range(n):
    x = randint(0, 1)
    if x == 0:
        el = stack.pop()
        print(el)
    else:
        el = int(input('element: '))
        stack.push(el)

print(stack)