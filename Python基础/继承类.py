class Person:
    def __init__(self,name,HairColor = 'white'):
        self.name = name
        self.color = HairColor
    def running(self):
        print("%s is shouting!"%self.name)
    def eat(self):
        print('eating')

#继承类（子类）
# class son(Person):
class Son():
    def __init__(self,Name,SkinColor):
        self.color = SkinColor
        self.name = Name
    def dancing(self):
        print('He can dance!')
    def run(self):
        print('%s is execising'%self.name)


# #创建子类对象
# Son = Son('Tom','Yellow')
# Son.dancing() #子类调用子类方法
# Son.run() #子类调用子类方法
# # Son.eat() #子类调用父类方法
#
# Edison = Person('Edison')
# Edison.running() #父类调用父类方法

#多继承类
class Brother(Person,Son):
    def sing(self):
        print('%s is singing'%self.name)

Kyle = Brother('Kyle')
Kyle.run()
Kyle.sing()
