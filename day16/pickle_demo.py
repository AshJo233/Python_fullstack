#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Filename      :pickle_demo.py
@Description   :
@Datatime      :2020/09/07 12:57:06
@Author        :AshJo
@Version       :v1.0
"""


import pickle

l1 = [1, 2, 3]
# 将Python中所有的数据类型，转换成字节串，序列化过程
# 将字节串转换成python中数据类型，反序列化过程

# bys = pickle.dumps([1, 2, 3])
# print(bys)  # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
# print(type(bys))  # <class 'bytes'>


# 保存了元组的数据类型
# bys = pickle.dumps(l1)
# print(bys)
# print(type(bys))
# res = pickle.loads(bys)
# print(res)
# print(type(res))


# 所有的数据类型都可以进行序列化
# bys = pickle.dumps(set('abc'))
# res = pickle.loads(bys)
# print(res, type(res))


# 把pickle序列化内容写入文件中
# with open('c.txt', mode='wb') as f:
#     pickle.dump(l1, f)

# 从文件中反序列化pickle数据
# with open('c.txt', mode='rb') as f:
#     res = pickle.load(f)
#     print(res)
#     print(type(res))

# pickle常用场景：和json一样，一次性写入，一次性读取

# json，pickle的比较：
"""
json：
1.不是所有的数据类型都可以序列化（结果是字符串）
2.不能多次对同一个文件序列化
3.json数据可以跨语言

pickle：
1.所有的python类型都能序列化（结果是字节串）
2.可以多次对同一个文件序列化
3.不能跨语言
"""
