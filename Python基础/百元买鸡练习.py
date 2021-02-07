#a hundred buy chicken
sum = 100
for i in range (20):
    for k in range (33):
        for j in range (0,100,3):
            if i + k + j == sum and 5 * i + 3 * k + j/3 == sum:
                print("rooster:%d  hen:%d  chick:%d"%(i,k,j))

#Fibonacci sequence:1,1,2,3,5,8....
#f(x) = f(x-1) + f(x-2) show f(100)
fiblist = [1,1]
for i in range (2,100):
    fiblist.append(fiblist[i-1]+fiblist[i-2])
    print("the no.%d is %d"%(i+1,fiblist[i]))
print('f(100) = %d'%(fiblist[99]))
