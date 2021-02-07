class car: #创建对象
    def move(self): #定义方法
        print('The car is running..')

    def toot(self):
        print('The car is tooting')

BMW = car()
BMW.color = 'Black' #定义属性
BMW.oil = 30
BMW.move() #调用方法
BMW.toot()
print(BMW.color)
print(BMW.oil)

#定义类的属性
class Car: #创建对象
    def __init__(self,colour = 'Black'): #定义方法，给一个参数,默认值为black
        self.wheelNum = 4
        self.colour = colour

    def toot(self):
        print('The car is tooting')

Jaguar = Car()
print(Jaguar.colour)
# print(Aldi.wheelNum)
# print(Aldi.colour)
Land_Rover = Car('Red')
print(Land_Rover.colour)
# Land_Rover.colour = 'Red'
# print(Land_Rover.colour)

class Dog:
    def __init__(self,name,color = 'White'):
        self.color = color
        self.LegsNumb = 4
        self.name = name

    def Shout(self):
        print("Please cherish %s 's life!"%self.name)

Teddy = Dog('TITI','Brown')
print(Teddy.color)
print(Teddy.LegsNumb)
Teddy.Shout()

Labrador = Dog('VIVI','Yellow')
print(Labrador.color)
Labrador.Shout()

