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



