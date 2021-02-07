# filter function:
import math
def is_odd(n):
    return n % 2 == 1
nlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(nlist))
a = []
for i in nlist:
    a.append(i)
print(a)
# Traverse(遍历): to print all elements in a list one by one.
# Filtrating the numbers which the square root is integer in 1 - 100 numbers.
import math
def sqr_int(b):
    if math.sqrt(b) % 1 == 0:  # to judge if the quare root of numbers is integer.
        return b


nelist = filter(sqr_int, range(1, 101))
print(list(nelist))


# 大圣课程：
def a(x):
    if x > 0:
        return True
    else:
        return False

x = range(-10, 10)
print(x)
print(list(filter(a, x)))

def m(x):
    if x < 0:
        return x**2
    else:
        return x
print(list(map(m,x)))

# map function:
cube = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6]))
print(cube)
# to achieve addition between two lists
addit = list(map(lambda x, y: x + y, [1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9]))
print(addit)

# reduce function:
from functools import reduce

add = reduce(lambda x, y: 10 * x + y, [2, 5, 6])
print(add)
c = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)  # 100 is an original value
print(c)
