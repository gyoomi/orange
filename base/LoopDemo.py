#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/22 11:24
"""
i = 1
while i < 100:
    print(i)
    i += 1
"""
# 求1-100的和
"""
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("1-100的和为：", sum)
"""
# while嵌套
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1

    print("\n")
    i += 1
"""
# 九九乘法表
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%2d " % (j, i, i * j), end="")
        j += 1
    print("\n")
    i += 1
"""
"""
str = ""
for s in str:
    print(s)
else:
    print("没有数据")
"""
i = 1
while i < 6:
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1
    print("\n")
    i += 1


i = 4
while 0 < i < 5:
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1
    print("\n")
    i -= 1

