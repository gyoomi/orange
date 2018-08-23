#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/23 9:50
"""
for name in namesList:
    print(name)
"""
"""
i = 0
while i < len(namesList):
    print(namesList[i])
    i += 1
"""

# 添加元素
# append, extend, insert

# namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
# append()
# namesList.append(True)
# namesList.append(0)
# print(namesList)

# extend()
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# aList = [123, 'xyz', 'zara', 'abc', 123];
# bList = [2009, 'manni'];
# aList.extend(bList)
# print(aList)

# insert(index, object) 在指定位置index前插入元素object

# 修改元素("改")
# 查找元素("查"in, not in, index, count)
# #############################################################
# in（存在）,如果存在那么结果为true，否则为false
# not in（不存在），如果不存在那么结果为true，否则false
"""
findName = input("请输入你要查询的姓名：")
if findName not in namesList:
    print("对不起，你所查询的姓名在系统中不存在")
else:
    print("哈哈")
"""

"""
if findName in namesList:
    print("结果：" + findName)
else:
    print("对不起，你所查询的姓名不存在")
"""
# ################################################
# index, count
# index和count与字符串中的用法相同
# namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua', "xiaoMing", "xiaoMing"]
# print(namesList.index("xiaoMing", 4))

# ##############################################
# 删除元素("删"del, pop, remove)
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除

# namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua', "xiaoMing", "xiaoMing"]
# del namesList[3]
# print(namesList)

# 要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
# namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua', "xiaoMing"]
# namesList.pop(-2)
# namesList.pop()
# print(namesList)

# remove() 函数用于移除列表中某个值的第一个匹配项；没有返回值
namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua', "xiaoMing"]
namesList.remove("xiaoZhang")
# print(namesList)

# 排序(sort, reverse)
# list.sort(cmp=None, key=None, reverse=False)
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
# aList = [1, 4, 2, 3]
# aList.sort(reverse=True)
# print(aList)
# bList = [1, 4, 2, 3]
# bList.sort()
# print(bList)
# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort(reverse=True)
# print(vowels)

# reverse()
# aList = [123, 'xyz', 'zara', 'abc', 'xyz']
# aList.reverse()
# print(aList)

# 列表嵌套
# schoolNames = [['北京大学', '清华大学'], ['南开大学', '天津大学', '天津师范大学'], ['山东大学', '中国海洋大学']]
# i = 0
# while i < len(schoolNames):
#     j = 0
#     while j < len(schoolNames[i]):
#         print(schoolNames[i][j])
#         j += 1
#     print("-" * 20)
#     i += 1



















