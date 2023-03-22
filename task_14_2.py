from task_14_1 import Stack
from random import randint
from copy import deepcopy

def create_stack():
    stack = Stack()
    for _ in range(10):
        x = randint(0, 100)
        stack.push(x)

    return stack

def stack_length(stack):
    stack_copy = deepcopy(stack)
    counter = 0
    while not stack_copy.isEmpty():
        stack_copy.pop()
        counter += 1

    return counter

def stack_inverse(stack):
    inversed_stack = Stack()
    while not stack.isEmpty():
        x = stack.pop()
        inversed_stack.push(x)

    return inversed_stack

if __name__ == '__main__':
    stack = create_stack()
    print(stack_length(stack))
    print(stack)
    print(stack_inverse(stack))

