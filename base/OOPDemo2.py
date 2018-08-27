#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/27 21:30

# class Cat(object):
#
#     def __init__(self, name, color="白色"):
#         self.name = name
#         self.color = color
#
#     def run(self):
#         print("%s 在跑" % self.name)


# class BoSi(Cat):
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def eat(self):
#         print("%s  在吃" % self.name)
#
#
# b = BoSi("印度猫")
# print(b.name)
# print(b.color)
# b.eat()
# b.set_name("哈哈猫")
# b.run()
# b.eat()
# 子类在继承的时候，在定义类时，小括号()中为父类的名字
# 父类的属性、方法，会被继承给子类
#


# ##############################################
# 多继承
# class A:
#     def printA(self):
#         print("---A---")
#
#
# class B:
#     def printB(self):
#         print("---B---")
#
#
# class C(A, B):
#     def printC(self):
#         print("---C---")
#
#
# obj_c = C()
# obj_c.printA()
# obj_c.printB()
# obj_c.printC()

# ######################################
# class base(object):
#     def test(self):
#         print("---base test---")
#
#
# class A(base):
#     def test(self):
#         print("---A test---")
#
#
# class B(base):
#     def b(self):
#         print("b")
#
#
# class C(B, A):
#     pass
#
#
# obj_c = C()
# obj_c.test()
#
# print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.base'>, <class 'object'>)
# 若是父类中有相同的方法名，
# 而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法

# 重写父类方法与调用父类方法
# 结论：
# 是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法
# class Cat(object):
#     def sayhello(self):
#         print("hello, cat")
#
#
# class Bosi(Cat):
#     def sayhello(self):
#         print("hello, bosi")
#
#
# bosi = Bosi()
# bosi.sayhello()

# 调用父类的方法
# Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
# class Cat(object):
#     def __init__(self, name):
#         self.name = name
#         self.color = "yellow"
#
#
# class Persian(Cat):
#     def __init__(self, name):
#         # super().__init__(name)   python 3.x
#         super(Persian, self).__init__(name)
#
#     def get_name(self):
#         print(self.name)
#
#
# p = Persian("波斯猫")
# p.get_name()

# ##########################################33
# 多态
# 1.java或c#中类型(略)
# 2.Python “鸭子类型”
# class F1(object):
#     def test(self):
#         print("f1 test")
#
#
# class S1(F1):
#     def test(self):
#         print("s1 test")
#
#
# class S2(F1):
#     def test(self):
#         print("s2 test")
#
#
# def fun(obj):
#    obj.test()
#
#
# f1 = S1()
# fun(f1)
# f2 = S2()
# fun(f2)

# #########################################################
# 类属性、实例属性
# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

# 类属性
# class Person:
#     name = "tom"
#     __age = 22


# p = Person()
# print(p.name) 正确
# print(p.__age) 错误
# print(Person.name) 正确
# print(Person.__age) 错误

# 实例属性
# class Person(object):
#
#     address = "西安市" # 类属性
#
#     def __init__(self):
#         self.name = "jack" # 实例属性
#         self.age = 33      # 实例属性


# p = Person()
# p.age = 22
# print(p.address)
# print(p.name)
# print(p.age)

# print(Person.address) # 正确
# print(Person.name)    # 错误
# print(Person.age)     # 错误

# 通过实例(对象)去修改类属性

class Person(object):
    country = "china"


print(Person.country)
p = Person()
p.country = "japan"
print(p.country)     # 实例变量会屏蔽掉同名的类属性
print(Person.country)
del p.country
print("*" * 10)
print(p.country)     # china









