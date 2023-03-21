def sparce_matrix(func):

    def _sparce_matrix(*args):
        zeros = 0
        y = func(*args)
        for row in y:
            zeros += row.count(0)

        if zeros >= round(0.9*len(y[0])*len(y)):
            return {(y.index(row)+1, row.index(i)+1): 
                    i for row in y for i in row if i > 0}
        return y
    
    return _sparce_matrix


def input_matrix(n, m):
    matrix = [[0 for pos in range(m)] for row in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(input(f'M({i+1}, {j+1})'))

    return matrix

@sparce_matrix
def matrix_sum(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] += b[i][j]
    return a

if __name__ == '__main__':
    a = input_matrix(3, 2)
    b = input_matrix(3, 2)
    print(matrix_sum(a, b))
