#Anonymous Function
#Use Lambda to create Anonymous Function
Bar = lambda :'Shanghai'
print(Bar())

def calculation(number):
    return number + 1
result = calculation(555)
print(result)

res = lambda number:number + 1
result = res(123)
print(result)

#Lambda Function: The sum of three numbers
Cal = lambda x,y,z: x + y + z
print(Cal(1,2,3))

#Lambda Function: Find the even
even = lambda num: [i for i in num if i%2 == 0]
print(even([1,2,3,4,5,6,7,8,99,88]))

#The combination between def and lambda function
def fun(x):
    return lambda y: x + y
num = fun(22) # num = lambda y: 22 + y
print(num(44))

#Nested lambda function
num = lambda x: lambda y : x + y
fun = num (13)
print(fun(23))