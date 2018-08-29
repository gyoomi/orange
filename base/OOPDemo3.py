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
# try:
#     num = 33
#     print(num)
# except NameError as msg:
#     print("NameError occur: %s " % msg)
# else:
#     print("没有发生异常，真高兴！")

# try...finally...
import time


# try:
#     f = open("d:\\test.txt")
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     except:
#         print("读取的过程中发生了异常")
#     finally:
#         f.close()
#         print("关闭文件")
# except:
#     print("打开文件错误")

# ################################################################
# 异常的传递
# try嵌套中(略)

# 函数嵌套调用中
# 如果try嵌套，那么如果里面的try没有捕获到这个异常，那么外面的try会接收到这个异常，然后进行处理，如果外边的try依然没有捕获到，那么再进行传递。。。

# #########################################################################
# 抛出自定义的异常
# raise语句来引发一个异常。异常/错误对象必须有一个名字，且它们应是Error或Exception类的子类
# class ShortInputException(Exception):
#     def __init__(self, length, least):
#         super().__init__(self)
#         self.length = length
#         self.least = least
#
#
# def main():
#     try:
#         s = input("请输入 ---> ")
#         if len(s) < 3:
#             raise ShortInputException(len(s), 3)
#     except ShortInputException as msg:
#         print("ShortInputException:输入的长度是%d, 最小长度是%d" % (msg.length, msg.least))
#     else:
#         print("没有异常发生！")
#
#
# main()

# 关于代码#super().__init__()的说明
# 这一行代码，可以调用也可以不调用，建议调用，因为__init__方法往往是用来对创建完的对象进行初始化工作，
# 如果在子类中重写了父类的__init__方法，即意味着父类中的很多初始化工作没有做，这样就不保证程序的稳定了，
# 所以在以后的开发中，如果重写了父类的__init__方法，最好是先调用父类的这个方法，然后再添加自己的功能


# #############################################################################################
# 异常处理中抛出异常
# class Test:
#     def __init__(self, switch):
#         self.switch = switch
#
#     def calc(self, a, b):
#         try:
#             return a/b
#         except Exception as msg:
#             if self.switch:
#                 print("捕获开启，已经捕获到了异常，信息如下:")
#                 print(msg)
#             else:
#                 raise
#                 # 重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而触发默认的异常处理


# a = Test(True)
# a.calc(10, 0)

# b = Test(False)
# b.calc(10, 0)

# ##################################################################################
# 模块
# 模块制作
# <1>定义自己的模块
# 每个Python文件都可以作为一个模块，模块的名字就是文件的名字

# 模块中的__all__
# 1. 没有__all__
# 2. 模块中有__all__
# 如果一个文件中有__all__变量，那么也就意味着这个变量中的元素，不会被from xxx import *时导入

# ################################################################################
# python中的包


# import base.msg.sendmsg
# base.msg.sendmsg.sendmsg()
#
# import base.msg.revmsg
# base.msg.revmsg.revmsg()


from base.msg import *
sendmsg.sendmsg()
revmsg.revmsg()
