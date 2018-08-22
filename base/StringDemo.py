#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/22 17:00

string = "hello world"
"""
print[string[0]]
print[string[1]]
print[string[19]]
"""

# 切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作
abc = "abcdefg"
# print(abc[0:3])
# 实现反转字符的效果
# print(abc[::-1])
# print(abc[2::])
# print(abc[0:3:2])
# 截取前3个
# print(abc[:3])
# print(abc[1:])
# print(abc[::-2])

# find
# print(mystr.find("itcast", 0, 10))
# print(mystr.find("o", 0))

# index
# print(mystr.index("l", 0, 1))
# print(mystr.index("o", 0))

# count
# print(mystr.count("o", 5, 6))
# print(mystr.count("haha"))

# replace
# testStr = "my world ha ha h"
# testStr = testStr.replace("ha", "HA", 1)
# print(testStr)

test = "Line1-abcdef \nLine2-abc \nLine4-abcd"
# 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
# print(test.split())
# print(test.split(" ", 1))

# capitalize 将第一个单词变大写，其余变小写
# print("aBCDf".capitalize())
# test2 = "哈哈我是BACdfF"
# test2 = test2.capitalize()
# print(test2)

# title 标题化
# a = "hello world ha ha he xi"
# print(a.title())
# startswith
# endswith
# lower()转小写
# upper()转大写
# a = "hello world ha ha he xi"
# print(a.upper())

# ljust
# print(a.ljust(10))
# print(a.ljust(10, "t"))

# rjust
# print(a.rjust(11))
# print(a.rjust(13, "p"))

# center()
# print(a.center(50, "a"))

# strip()
# 它的函数原型：string.strip(s[, chars])，它返回的是字符串的副本，并删除前导和后缀字符。
# （意思就是你想去掉字符串里面的哪些字符，那么你就把这些字符当参数传入。此函数只会删除头和尾的字符，中间的不会删除。）
# 如果strip()的参数为空，那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)
# 传入多个字符参数,会当成一个个单个字符进行解析
a = "adahelloaca"
# print(a.strip())
# print(a.strip("a"))
# print(a.strip("abcd"))

# lstrip() 去除左边的
# rstrip() 去除右边的

mystr = 'hello world itcast and itcastcpp'
# rfind()
# print(mystr.rfind("or", 0, 10))
# print(mystr.rfind("or", 0))
# print(mystr.rfind("or", 10))

# rindex()和index类似，只是从右边开始
# 如果包含子字符串返回开始的索引值，否则抛出异常
# b = "hello welcome itcast cp school"
# print(b.rindex("IT"))
# print(b.rindex("itcast"))

# partition()
# rpartition()
# 返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串
# c = "hello welcome itcast itcast cp school"
# print(c.partition("itcast"))
# print(c.rpartition("itcast"))
"""
('hello welcome ', 'itcast', ' itcast cp school')
('hello welcome itcast ', 'itcast', ' cp school')
"""

# splitlines()
# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
# 如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# d = "hello \n world \r   \r\n "
# print(d.splitlines(True))
# print(d.splitlines(False))

# isalpha()
#  方法检测字符串是否只由字母组成
# e = "ljlrwwrwr12323434?"
# print(e.isalnum())

# isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False
# f1 = "324"
# f2 = "324a3"
# f3 = "we"
# print(f1.isdigit())
# print(f2.isdigit())
# print(f3.isdigit())












