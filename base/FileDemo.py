#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leon
# @Version : 2018/8/26 22:33

# 创建文件和关闭文件
# f = open("d://test.txt", "w")
#
# 关闭文件
# f.close()

# 写文件
# 如果文件不存在那么创建，如果存在那么就先清空，然后写入数据
# f = open("d://text.txt", "w")
# f.write("hello python3 i am here!")
# f.close()

# 读文件
f = open("d:\\text.txt")
content = f.read(5)
print(content)
print("-" * 20)
content = f.read()
print(content)



