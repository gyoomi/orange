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
# f = open("d:\\text.txt")
# content = f.read(5)
# print(content)
# print("-" * 20)
# content = f.read()
# print(content)

# 读数据（readlines）
# f = open("d:\\test.txt")
# content = f.readlines()
#
# print(content)
# for item in content:
#     print(item, end="")
# # print(type(content))
# f.close()

# 读数据（readline）
# f = open("d:\\test.txt", "r")
# content = f.readline()
# print("1:%s" % content)
# content = f.readline()
# print("2:%s" % content)
# f.close()

# 应用
# 输入文件的名字，然后程序自动完成对文件进行备份
# oldFileName = input("请输入要拷贝的文件名称：")
# oldFile = open(oldFileName)
# if oldFile:
#     fileExtIndex = oldFileName.rfind(".")
#     if fileExtIndex > 0:
#         fileExt = oldFileName[fileExtIndex:]
#     newFileName = oldFileName[:fileExtIndex] + "复制" + fileExt
#     newFile = open(newFileName, "w")
#     for content in oldFile.readlines():
#         newFile.write(content)
#     oldFile.close()
#     newFile.close()

# 文件的定位读写
# 如果想知道当前的位置，可以使用tell()来获取
# f = open("d://test.txt", "r")
# content = f.read(3)
# print("读取的数据是：" + content)
#
# position = f.tell()
# print("位置是：" + str(position))
#
# content = f.read(3)
# print("读取的数据是：" + content)
#
# position = f.tell()
# print("位置是：" + str(position))


# 需要从另外一个位置进行操作的话，可以使用seek()
# fileObject.seek(offset[, whence])
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数；
# whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

# f = open("d:\\test.txt", "r")
# content = f.read(10)
# print(content)
# position = f.tell()
# print("当前位置是：%d" % position) # 11
# f.seek(5, 0)
# position = f.tell()
# print("当前位置是：%d" % position)  # 5
# f.close()

# f = open("d:\\test.txt", "r")
# content = f.read(10)
# print(content)
# position = f.tell()
# print("当前位置是：%d" % position) # 11
# f.seek(-4, 2)
# position = f.tell()
# print("当前位置是：%d" % position)  # 5
# f.close()

# 有些时候，需要对文件进行重命名、删除等一些操作，python的os模块中都有这么功能
# 文件重命名
import os

# os.rename("d:\\test.txt", "d:\\test22.txt")

# 删除文件
# os.remove("d:\\test22.txt")

# 文件夹的相关操作
# 创建文件夹
# os.mkdir("d:\\test222")

# 获取当前目录
# print(os.getcwd())

# 改变默认目录
# os.chdir("../")

# 获取目录列表
# print(os.listdir("d:\\"))

# 删除文件夹
# os.rmdir("d:\\test222")

# ############################################
# 批量修改文件名字
# funFlag = 1 # 1添加标记 2 删除标记
# folderName = "d:\\test\\"
# fileList = os.listdir(folderName)
# for f in fileList:
#     if funFlag == 1:
#         newName = "[明哥出品]-" + f
#     elif funFlag == 2:
#         index = len("[明哥出品]-")
#         newName = f[index:]
#
#     os.rename(folderName + f, folderName + newName)

# 读取一个文件，显示除了以井号(#)开头的行以外的所有行
# readFileName = input("请输入要读取的文件：")
# readFile = open(readFileName)
# for item in readFile.readlines():
#     if not item.startswith("#"):
#         print(item)
# readFile.close()










