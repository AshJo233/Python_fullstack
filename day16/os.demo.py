#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :os.demo.py
@Description   :操作系统模块
@Datatime      :2020/09/06 13:31:12
@Author        :AshJo
@Version       :v1.0
'''

# 和操作系统相关的操作都被封装到这个模块中

import os


# 删除文件
# os.remove(r'day16\a.txt')
# os.remove('b.txt')


# 文件重命名
# os.rename(r'day16\a.txt',r'day16\b.txt')

# 删除目录，只能删除空目录
# os.removedirs('aa')


# 使用shutil模块可以删除带内容的目录
# import shutil
# shutil.rmtree('aa')

# 和路径相关的操作，被封装到另一个子模块中：os.path
# res = os.path.dirname(r'd:/aaa/bbb/ccc/a.txt') # 不判断路径是否存在
# print(res)

# # 获取文件名
# res = os.path.basename(r'd:/aaa/bbb/ccc/a.txt')
# print(res)

# 把路径中的路径名和文件名切割成元组数据存放
# res = os.path.split(r'd:/aaa/bbb/ccc/a.txt')
# print(res)


