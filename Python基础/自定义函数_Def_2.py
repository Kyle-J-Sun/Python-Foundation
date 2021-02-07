#Random Int
import random
print(random.randint(1,100))

#list shuffle
a = [1,2,3,4,5,6,7,8]
random.shuffle(a)
print(a)
#Random float
print(round(random.random(),2))
print(random.uniform(0.1,0.3))

#Random slice
list1 = [1,4,2,4,5,5,6,3,6,7,7,7]
slice = random.sample(list1,5)
print(slice)

#Random Tele Number
def rand():
    a = random.randint(10000000000,19999999999)
    print('Congratulations to ' + str(a))
rand()

#Double Colour Ball Lottery(Red ball : six numbers, no repeat Blue Ball: one number )
#Method 1
def doubleballs():
    import random
    ball = []
    while True:
        num = random.randint(1,33)
        if num in ball:
            continue
        else:
            ball.append(num)
        if len(ball) == 6:
            break
    ball.sort()
    ball.append(random.randint(1,16))
    print(ball)
doubleballs()
# Method 2
def doubleballs2():
    import random
    red = list(range(1,34))
    ball = random.sample(red,6)
    ball.sort()
    ball.append(random.randint(1,16))
    print(ball)
doubleballs2()
