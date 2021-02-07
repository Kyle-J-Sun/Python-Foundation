#iterator: an object that can remember the position of traverse.
iter() #create an iterator
next() #return the next event of iterator
list = [1,2,3,4]
it = iter(list)
for i in range(10):
    x = next(it,'No default value')
    print(x)

#builder: builder is a function of returning iterators.
import sys
def fib(n):
    a,b,con = 0,1,0
    while True:
        if (con > n ):
            return
        yield a,b
        a,b = b,b+a
        con += 1

f = fib(10)
while True:
    try:
        print(next(f))
    except StopAsyncIteration:
        sys.exit()

#recursion: in the process of invoking function, directly or indirectly invoke the function itself.
def fun():
    return fun()

def facto(n):
    if n == 1:
        return 1
    return n * facto(n - 1)
facto(5)
#5*fact(4)-->5*4*fact(3)-->5*4*3*fact(2)-->5*4*3*2*fact(1)-->5*4*3*2*1
print(facto(5));

def func(y):
    print (y) #10 5 2.5 1.25
    if y/2 > 1:
        rep = func(y/2) #
    print('last recurring value:',y)
    return y

func(10)

def num(i):
    print(i)
    if i/2 > 1:
        print(i/2)
        if i/4 > 1:
            print(i/4)
            if i/8 > 1:
                print(i/8)
                print('last recursion:',i/8)
            print('last recursion:',i/4)
        print('last recursion:',i/2)
    print('last recursion:',i)

num(10)