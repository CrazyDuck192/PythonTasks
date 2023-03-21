from start.rational_numb import *

k = int(input())
my_rationals = [rat_inp() for _ in range(k)]

print(1/sum(my_rationals))




