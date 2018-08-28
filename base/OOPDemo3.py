#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/28 10:19
# #######################################
# 工厂模式之简单工厂和工厂方法模式


class Audi(object):

    def move(self):
        print("车在移动")

    def stop(self):
        print("刹车了")


class BMW(object):
    def move(self):
        print("车在移动")

    def stop(self):
        print("刹车了")


class CarFactory(object):

    def create_car(self, type):
        if type == "奥迪":
            car = Audi()
        elif type == "宝马":
            car = BMW()
        return car


class CarStore(object):
    def __init__(self):
        self.car_factory = CarFactory()
        #  设置4s店的指定生产工厂

    def order(self, type):
        car = self.car_factory.create_car(type)
        return car


store = CarStore()
c = store.order("宝马")
c.move()
c.stop()