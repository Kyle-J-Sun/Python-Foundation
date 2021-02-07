list1 = [1,1,1,2]
print(list1[4])

list1 = [1,1,1,2]
try:
    print(list1[4])
except BaseException as Err:
    print(Err)
finally:
    print('end')

def hello():
    print('hi')
    print('Kyle')
    name = input('Type your name here!')
    if name == 'Kyle':
        print('Yes')

hello()

def hello(name):
    print('Hi!' + name)

hello('Kyle')

