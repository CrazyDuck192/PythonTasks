from math import sqrt
from cw1 import *

p_1 = float(input('p = '))
q_1 = float(input('q = '))

D = p_1**2 - 4*q_1
x_1 = (-p_1 - sqrt(D)) / 2
x_2 = (-p_1 + sqrt(D)) / 2

t1 = set_segment(x_1, x_2)

p_2 = float(input('p = '))
q_2 = float(input('q = '))

D = p_2**2 - 4*q_2
x_1 = (-p_2 - sqrt(D)) / 2
x_2 = (-p_2 + sqrt(D)) / 2

t2 = set_segment(x_1, x_2)

print(intersect(t1, t2))

