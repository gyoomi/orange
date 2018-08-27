#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/27 15:33


# class Car:
#     def toot(self):
#         print("汽车在鸣笛！")
#
#     def move(self):
#         print("汽车正在移动...")
#
#
# bm = Car()
# bm.color = "黑色"
# bm.price = "35W"
# print(bm.color)
# print(bm.price)
# bm.move()
# bm.toot()

# __init__()方法
#
# class Car:
#     def __init__(self, color, price):
#         self.color = color
#         self.price = price
#
#     def toot(self):
#         print("汽车有知识产权")
#
#     def move(self):
#         print(self.color + "汽车在奔跑...")
#
#
# bm = Car("白色", "Audi")
# print(bm.color)
# print(bm.price)

# 魔法方法
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def move(self):
        print(self.color + "的" + self.brand + "汽车在公路上狂奔...")

    def __str__(self):
       msg = self.color + "的" + self.brand + "汽车"
       return msg


bm = Car("黑色", "宝马")
# bm.move()
# print(bm)

# self类似于c++、java中的this
# python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面的参数即可


# class Potato:
#
#     def __init__(self):
#         self.cookedLevel = 0
#         self.cookedString = "生的"
#         self.condiments = []
#
#     def cook(self, time):
#         self.cookedLevel += time
#         if self.cookedLevel > 8:
#             self.cookedString = "烤成灰了"
#         elif self.cookedLevel > 5:
#             self.cookedString = "烤好了"
#         elif self.cookedLevel > 3:
#             self.cookedString = "半生不熟"
#         else:
#             self.cookedString = "还是生的"
#
#     def addConditon(self, condiment):
#         self.condiments.append(condiment)
#
#     def __str__(self):
#         msg = self.cookedString + "地瓜"
#         if len(self.condiments) > 0:
#             msg += "("
#             for item in self.condiments:
#                 msg += item + ","
#             msg.strip(",")
#             msg += ")"
#         return msg
#
#
# sweetPotato = Potato()
# print(sweetPotato)
# sweetPotato.cook(2)
# print(sweetPotato)
# sweetPotato.cook(2)
# print(sweetPotato)
# sweetPotato.cook(2)
# print(sweetPotato)

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         if len(name) > 5:
#             self.__name = name
#         else:
#             print("error:名字长度需要大于或者等于5")
#
#
# p = Person("小明")
# print(p.get_name())

# __del__()方法
# 创建对象后，python解释器默认调用__init__()方法；
# 当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法

































