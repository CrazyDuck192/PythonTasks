class Deque:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return not self.data

    def add_left(self, element):
        self.data.insert(0, element)

    def pop_left(self):
        return self.data.pop(0)

    def add(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

class Stack:

    def __init__(self):
        self.data = Deque()

    def is_empty(self):
        return self.data.is_empty()

    def push(self, element):
        self.data.add(element)

    def pop(self):
        return self.data.pop()

    def __str__(self):
        return str(self.data.data)



def fill_stack(stack):
    n = int(input('Кількість елементів: '))
    for _ in range(n):
        x = int(input('Елемент: '))
        stack.push(x)

def inverse_stack(stack1, stack2 = Stack()):
    while not stack1.is_empty():
        el = stack1.pop()
        stack2.push(el)

    return stack2


if __name__ == "__main__":
    st = Stack()
    fill_stack(st)
    print(st)

    st = inverse_stack(st)
    print(st)