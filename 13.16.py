from collections import defaultdict
from random import randint
from math import ceil

def create():
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    sparce_matrix = defaultdict(int)
    vector = [0 for _ in range(5)]
    sparce_vector = defaultdict(int)
    nonzero_elements = 0

    while nonzero_elements < ceil(0.1*len(matrix)**2):
        i = randint(1, len(matrix)-1)
        j = randint(1, len(matrix)-1)
        if (i+1, j+1) not in sparce_matrix.keys():
            sparce_matrix[(i+1, j+1)] = randint(1, 10)
            nonzero_elements += 1
    nonzero_elements = 0

    while nonzero_elements < ceil(0.1*len(vector)):
        i = randint(1, len(vector)-1)
        if (i+1, 1) not in sparce_vector.keys():
            sparce_vector[(i+1, 1)] = randint(1, 10)
            nonzero_elements += 1
    
    return sparce_matrix, sparce_vector


def find_max(sparce_matrix):
    return f'Максимальний елемент розрідженої матриці: {max(sparce_matrix.values())}'

def multiply(sparce_matrix, sparce_vector):
    new_vector = defaultdict(int)
    for x in sparce_matrix.keys():
        for y in sparce_vector.keys():
            if x[1] == y[0]:
                new_vector[(x[0], y[1])] += sparce_matrix[x]*sparce_vector[y]

    return new_vector

def is_lower(sparce_matrix):
    for pos in sparce_matrix.keys():
        if pos[0] < pos[1]:
            return 'Розріджена матриця не є нижньою трикутною'
    return 'Розріджена матриця є нижньою трикутною'

if __name__ == '__main__':
    matrix, vector = create()
    print(matrix)
    print(vector)

    print(find_max(matrix))

    print(multiply(matrix, vector))

    print(is_lower(matrix))
