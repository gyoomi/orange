#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/28 10:19
# #######################################
# 工厂模式之简单工厂和工厂方法模式

# 简单工厂
# class Audi(object):
#
#     def move(self):
#         print("车在移动")
#
#     def stop(self):
#         print("刹车了")
#
#
# class BMW(object):
#     def move(self):
#         print("车在移动")
#
#     def stop(self):
#         print("刹车了")
#
#
# class CarFactory(object):
#
#     def create_car(self, type):
#         if type == "奥迪":
#             car = Audi()
#         elif type == "宝马":
#             car = BMW()
#         return car
#
#
# class CarStore(object):
#     def __init__(self):
#         self.car_factory = CarFactory()
#         #  设置4s店的指定生产工厂
#
#     def order(self, type):
#         car = self.car_factory.create_car(type)
#         return car
#
#
# store = CarStore()
# c = store.order("宝马")
# c.move()
# c.stop()


# 工厂方法
# class Audi(object):
#
#     def move(self):
#         print("Audi move...")
#
#     def stop(self):
#         print("Audi stop...")
#
#
# class Jeep(object):
#
#     def move(self):
#         print("Jeep move...")
#
#     def stop(self):
#         print("Jeep stop...")
#
#
# class CarFactory:
#
#     def get_car(self, type):
#         if type == "奥迪":
#             car = Audi()
#         elif type == "吉普":
#             car = Jeep()
#
#         return car
#
#
# class CarStrore(object):
#
#     def create_car(self, type):
#         pass
#
#     def order(self, type):
#         self.car = self.create_car(type)
#         self.car.move()
#         self.car.stop()
#
# class AudiStore(CarStrore):
#
#     def create_car(self, type):
#         self.car_factory = CarFactory()
#         return self.car_factory.get_car(type)
# class JeepStore(CarStrore):
#
#     def create_car(self, type):
#         self.car_factory = CarFactory()
#         return self.car_factory.get_car(type)
#
#
# # audi = AudiStore()
# # audi.order("奥迪")
#
# jStore = JeepStore()
# jStore.order("吉普")

# ##########################################################
# __new__方法
# __new__和__init__的作用__new__和__init__的作用
# class A(object):
#     def __init__(self):
#         print("这是init()方法")
#
#     def __new__(cls, *args, **kwargs):
#         print("这是new()方法")
#         return object.__new__(cls)

# __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
# __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# 我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节


# a = A()

# ########################################################
# 单例模式


# class Sington(object):
#
#     __instance = None
#
#     def __new__(cls, name, age):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#
# a = Sington("tom", 19)
# b = Sington("jack", 29)
# print(id(a))
# print(id(b))

# a.age = 99
# print(b.age)

# 创建单例时，只执行1次__init__方法
# 实例化一个单例
# class Singleton(object):
#     __instance = None
#     __first_init = False
#
#     def __new__(cls, name, age):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def __init__(self, name, age):
#         if not self.__first_init:
#             self.name = name
#             self.age = age
#             Singleton.__first_init = True
#
#
# a = Singleton("tom", 22)
# b = Singleton("jack", 11)
# print(a.name)
# print(b.name)

# #########################################################################
# 异常
# 发生异常
# open("d:\\123.txt", "r")

# 捕获异常 try...except...

# try:
#     print("--test start-")
#     open("d:\\123.txt", "r")
#     print("--test   end-")
# except IOError:
#     pass

# #######################################################3
# except捕获多个异常

# try:
#     print(num)
# except (NameError, IOError) as msg:
#     # 如果想通过一次except捕获到多个异常可以用一个元组的方式
#     print(msg)

# try:
#     # print(num)
#     # open("d:\\324.txt")
#     a = 10 / 0
# except NameError:
#     print("NameError: variable is not defined")
# except IOError:
#     print("IOError: the file not exist!")
# except:
#     print("Unexpected occur!!!")
#     raise

# 捕获所有异常
# try:
#     print(num)
# except:
#     print("异常产生了")

# else
# 同样在try...except...中也是如此，即如果没有捕获到异常，那么就执行else中的事情
















