i = 0
while i<100:
    print('this is %d' % (i+1))
    break
    i = i + 1
print('That\'s the end')


while True :
    account = {'root':'123456'}
    usrname = input("Username:")
    pasword = input("Password:")
    if usrname in account.keys() and pasword == account[usrname]:
        print('Login successfully!')
        break
    else:
        print('The username cannot be found or password is not correct')

i = 0
while i < 3 :
    account = {'root':'123456'}
    usrname = input("Username:")
    pasword = input("Password:")
    if usrname in account.keys() and pasword == account[usrname]:
        print('Login successfully!')
        break
    else:
        i += 1
        if i != 3:
            print('The username cannot be found or password is not correct, you have %d chance left!' % (3-i))
        else:
            print('Your account has been locked!')

for i in range (100):
    print(i)

for i in range (3,100):
    print(i)

for i in range (2,100,4):
    print(i)

#For function is used to iterate elements of the container.
#it could be lists, tuples, dictionary, files and sets.
# Iteration : the process to read elements from the container one by one.
# It won't stop until the elements are read completely.

for i in 'Kyle':
    print(i, end = ' ');

for i in range (100):
    print('This is %d' % i)
print('That is the end')

# Use WHILE function to output 1,2,3,4,5,6,8,9,10

i = 0
while i < 6:
    i = i + 1
    print(i)
j = 7
while j < 10:
    j = j + 1
    print(j)


i = 0
while i < 10:
    i += 1
    if i != 7:
        print(i)


# The sum of 1-100

ii = 0
lst = []
while ii < 100:
    ii = ii + 1
    lst.append(ii)
print(sum(lst))


sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(sum)


# All of odds between 1 and 100

i = 0
while i < 50:
    i += 1
    j = i + (i - 1)
    print(j)

i = 0
while i < 101:
    if i%2 == 1:
        print(i)
    i = i + 1


#For 'for' function:
#Show all odds in the list 1 one by one, which list 1 = [1,2,3,4,5,6,7]
list1 = [1,2,3,4,5,6,7]
list2 = []
for i in range(list1[0],len(list1)+1,2):
    list2.append(i)
print(list1,list2)

#Show the intersection numbers between list1 and list2

list1 = [1,2,3,4,5,6,7]
list2 = [1,3,5,7]
list3 = []
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)


for i in range(1,int(input('Please type a number:')) + 1,2):
    print(i, end = " ")
    if (i + 1) % 20 == 0:
        print()