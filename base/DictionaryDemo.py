#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/23 22:32
import operator
# Dictionary 字典 类似于Java中map
# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# 根据键访问值
# print(info["name"])
# print(info["address"])
# 设置默认值
# print(info.get("sex1", "m"))

# 修改元素
# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# newId = input("请输入新学号：")
# info["id"] = int(newId)
# print(info)

# 添加元素
# 删除元素
# del  clear
# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# del info["id"]
# print(info)

# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# print("清空前：%s" % info)
# info.clear()
# print("清空后：%s" % info)

# len()
# 测量字典中，键值对的个数
# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# print(len(info))

# keys 返回一个包含字典所有KEY的列表
# values 返回一个包含字典所有value的列表

# items
# 返回一个包含所有（键，值）元组的列表
# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# rs = info.items()
# print(rs)
#
# for k, v in rs:
#     print("结果是：%s  %s" % (k, v))

# has_key   __contains__
# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
# print(info.__contains__("name"))
# print(info.__contains__("name2"))

# 字符串遍历
# a_str = "hello itcast"
# for s in a_str:
#     print(s)

# 列表遍历
# a_list = [1, 2, 3, 4, 5]
# for item in a_list:
#     print(item, end=' ')

# 元组遍历
# a_turple = (1, 2, 3, 4, 5)
# for item in a_turple:
#     print(item, end=" ")

# 遍历字典的项（元素）
# dictionary = {"name": "张三", "id": 22}
# for item in dictionary.items():
#     print(item)

# 遍历字典的key-value（键值对）
# dictionary = {"name": "张三", "id": 22}
# for k, v in dictionary.items():
#     print("%s %s" % (k, v))

# enumerate()
# Python 2.3. 以上版本可用，2.6 添加 start 参数。
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# print(list(enumerate(seasons, start=1)))

# seq = ['one', 'two', 'three']
# for i, e in enumerate(seq):
#     print("%s : %s" % (i, e))

# ################################################
# 公共方法
# + 合并 字符串、列表、元组
# * 复制 字符串、列表、元组
#

# cmp
# cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# python3 没有此模块，引入了新的operator模块
# a = 100
# b = 99
# c = 101
# print(operator.eq(a, b))
# print(operator.lt(a, b))
# print(operator.gt(a, b))
# print(operator.gt("awrwe3r423423234we34sfdfsr", "b234234a"))

# #####################################################################
# 引用相关
# a = 1
# b = a
# a = 2
# print(b)

# 可变类型，值可以改变：
# 列表 list
# 字典 dict

# 不可变类型，值不可以改变：
# 数值类型 int, long, bool, float
# 字符串 str
# 元组 tuple

# 使用id()函数查看其类似于内存地址的号码

# 练习
# 怎样交换两个变量的值？
a = 1
b = 8

a = a + b
b = a - b
a = a - b
print(a)
print(b)





