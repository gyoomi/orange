#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/24 22:35

# 1.编程实现对一个元素全为数字的列表，求最大值、最小值
# aList = [-22, 9, 0, 23, 89]
# print(max(aList))
# print(min(aList))
#
# print("-" * 20)

# 2.统计字符串中，各个字符的个数
# rs = {}
# aStr = "hello world"
# for s in aStr:
#     if rs.__contains__(s):
#         rs[s] += 1
#     else:
#         rs[s] = 1
# print(rs)
# print("-" * 20)

# 完成一个路径的组装
# 先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share
i = 0
path = ""
while i < 3:
    t = str(input("请输入第" + str(i + 1) + "次路径名："))
    path = path + t
    i += 1
print(path)
