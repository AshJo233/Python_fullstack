#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Filename      :collections_demo.py
@Description   :
@Datatime      :2020/09/07 15:34:01
@Author        :AshJo
@Version       :v1.0
"""

# import collections
from collections import *

# 命名元组 namedtuple()  （类似字典）
Rectangle = namedtuple('Rectangle_class', ['length', 'width'])
r = Rectangle(10, 5)
# 通过属性访问元组
# r.length = 4
print(r.length)
print(r.width)

# 通过索引访问元组
print(r[0])
print(r[1])

# 默认字典 defaultdict:

# d = {k: v for k, v in [(1, 3), (2, 4)]}
# print(d)

# d = defaultdict(int, name='Andy', age=18)
# print(d['name'])
# print(d['age'])
# print(d['address'])     # {'address': 0}也会被添加
# print(d)

# 自定义函数充当一个参数
# 要求，不能有参数


def f():
    return 'None'


d = defaultdict(f, ame='Andy', age=18)
print(d['name'])
print(d['age'])
print(d['address'])     # {'address': 0}也会被添加
print(d)

# Counter: 计数器
c = Counter('abcessdfsafvcfssdfsdddfd')
print(c)
print(c.most_common(3))
