from collections import deque
from copy import copy

class Stack:

    def __init__(self):
        self.data = deque()

    def isEmpty(self):
        return not self.data

    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        return self.data.pop()
    
    def __str__(self) -> str:
        return f"stack[{', '.join(str(x) for x in self.data)}]"
    
def sort_sequence(seq):
    seq_copy = copy(seq)
    stack_1 = Stack()
    stack_2 = Stack()
    while seq:
        el = seq.pop(0)
        stack_1.push(el)
    while not stack_1.isEmpty() or not stack_2.isEmpty():
        if stack_2.isEmpty():
            while not stack_1.isEmpty():
                el = stack_1.pop()
                if el == min(seq_copy):
                    seq.append(el)
                    seq_copy.remove(el)
                else:
                    stack_2.push(el)

        elif stack_1.isEmpty():
            while not stack_2.isEmpty():
                el = stack_2.pop()
                if el == min(seq_copy):
                    seq.append(el)
                    seq_copy.remove(el)
                else:
                    stack_1.push(el)

    return seq
    
if __name__ == '__main__':
    seq = [4, 3, 6, 9, 10, 1, 2, 8, 4, 5, 1, 1, 11]
    print(sort_sequence(seq))