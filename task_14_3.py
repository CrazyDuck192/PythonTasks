from collections import deque
from copy import deepcopy
from random import randint

class Queue:

    def __init__(self):
        self.data = deque()

    def is_empty(self):
        return not self.data
    
    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.popleft()
    
    def __str__(self) -> str:
        return f"queue[{', '.join(str(x) for x in self.data)}]"

def create_queue():
    q = Queue()
    for _ in range(10):
        x = randint(0, 100)
        q.push(x)

    return q

def queue_length(q):
    counter = 0
    tmp = deepcopy(q)
    while not tmp.is_empty():
        tmp.pop()
        counter += 1

    return counter

def queue_recursive_length(q, q_list=[]):
    if q.is_empty():
        return 0
    
    el = q.pop()
    length = 1 + queue_recursive_length(q) 
    q_list.append(el)
    q.data = reversed(q_list)
    
    return length


if __name__ == '__main__':
    q = create_queue()
    print(q)
    print(queue_length(q))
    print(queue_recursive_length(q))
    print(q)
