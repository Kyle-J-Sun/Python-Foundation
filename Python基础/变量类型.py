#Global Variable and Local Variable
x = 200
def func():
    global x  #Declare global variable
    x = 100
    print(x)

func()
print('func outside',x)

total = 0
def sum(x,y):
    total = x + y
    print(total)
    return total

def toprint():
    print(total)

print(sum(10,20))
sum(10,20)

print(toprint())
toprint()

print(total)

#To judge if the object is iterable
from collections import Iterable
print(isinstance('abc',Iterable))

import collections
print(isinstance([1,2,3],collections.Iterable))

import collections
print(isinstance(123,collections.Iterable))

#Filter() Function
def find_odds(n):
    return n%2 == 1
lst=filter(find_odds,[1,2,3,4,5,6,7,8,9])
print(lst)
lst2 = []
for i in lst:
    lst2.append(i)
print(lst2)