for j in range(1,10):
    print()
    for i in range(1,10):
        tab = j * i
        if j >= i:
            print('%d*%d=%d'%(j,i,tab), end=" ")

for i in range(1,10):
    for j in range(1,i + 1):
        print('%d*%d=%d' % (j, i, i * j), end=" ")
        print()

for i in range(0,10):
    print('*' * (i + 1))
