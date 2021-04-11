# 在C++中使用如下3个条件实现多态
# 1、虚函数从写
# 2、父类指针指向子类对象
# 3、继承
# python 3.6中也可以使用方便使用抽象类 from abc import ABC,abstractmethod
from abc import ABC, abstractmethod


class Handller(ABC):  # 抽象类
    @abstractmethod  # 指定为接口函数 类似C++的纯虚函数
    def test(self):
        pass


# 两个类继承来自同一个抽象类
class ChildOne(Handller):  # 继承
    def __init__(self, b, c):
        self.name = b
        self.age = c

    def test(self):  # 类似C++虚函数重写函数
        print("this is test {} {}".format(self.name, self.age))


class ChildTwo(Handller):  # 继承

    def __init__(self, a):
        self.name = a

    def test(self):  # 类似C++虚函数重写函数
        print("this is test {}".format(self.name))


class DoThing:
    @staticmethod
    def test_do_thing(handler):  # 统一调用接口
        handler.test()


a = ChildOne('Dan', 30)
b = ChildTwo('Dan')
DoThing.test_do_thing(a)  # 多态 父类指针指向子类对象
DoThing.test_do_thing(b)  # 多态 父类指针指向子类对象
