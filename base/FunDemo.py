#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/24 22:58
# def printInfo():
#     print("-" * 20)
#     print("---人生苦短，我用python---")
#     print("-" * 20)
#
# printInfo()

# def test(a, b):
#     print("%d" % (a + b))
# # test(11, 22)
# help(test)


# def add2num(a, b):
#     return a + b
#
#
# result = add2num(98, 234)
# print(result)

# a = 100
#
#
# def test():
#     # 方法中修改全局变量
#     global a
#     a += 50
#     print(a)

#
# def test02():
#     print(a)
#
#
# test02()
# test()

# 函数，多个返回值
# def test(a, b):
# #     ji = a * b
# #     sum = a + b
# #     chu = a / b
# #     return ji, sum, chu
# #
# #
# # print(test(10, 2))

# 函数参数：缺省函数
# 注意：带有默认值的参数一定要位于参数列表的最后面。
# def printinfo(name, age=35):
#     print(name + ":" + str(age))
# printinfo("tom")
# printinfo("jack", 22)

# 不定长参数
# 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；
# 而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。
# 注意调用的时候，加*和不加*的区别
# foo("你", "好", *tuples, **info)
# foo("你", "好", tuples, info)
# def foo(a, b, *args, **kwargs):
#     print("*" * 20)
#     print("a = " + a)
#     print("b = " + b)
#     print("args = " + str(args))
#     print("kwargs = ")
#     for k, v in kwargs.items():
#         print(k + "=" + str(v))
#     print("*" * 20)
#
#
# tuples = ("hello", "world")
# info = {"id": 199234, "name": "杰克"}
# foo("你", "好", *tuples, **info)

# Python中函数参数是引用传递（注意不是值传递）。对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；
# 而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。
# a_int = 12
# def foo(a):
#     a += a
#     return a
#
#
# print(foo(a_int))
# print(a_int)

# a = []
# def bar(args):
#     args.append("hello")
#     print(args)
#
# bar(a)
# print(a)

# 递归函数
# 我们来计算阶乘 n! = 1 * 2 * 3 * ... * n

# 使用while来完成递归计算
# def jc(num):
#     i = 1
#     result = 1
#     while i <= num:
#         result *= i
#         i += 1
#     return result
#
#
# print(jc(4))

# 使用递归计算
# def caljc(num):
#     if num == 1:
#         return 1
#     else:
#         return caljc(num - 1) * num
#
#
# print(caljc(4))

# 用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。
# lambda [arg1 [,arg2,.....argn]]:expression
# 注意：
# Lambda函数能接收任何数量的参数但只能返回一个表达式的值
# 匿名函数不能直接调用print，因为lambda需要一个表达式

# sum = lambda a, b: a + b
# print(sum(1, 11))

# 应用场景
# 函数作为参数传递
def foo(a, b, opt):
    print("a = %s" % a)
    print("b = %s" % b)
    return opt(a, b)


rs = foo(18, 4, lambda x, y: x + y)
print(rs)

import time

print(time.time())





