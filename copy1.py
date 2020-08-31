#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :copy.py
@Description   :
@Datatime      :2020/08/20 14:45:24
@Author        :AshJo
@Version       :v1.0
'''


# 赋值运算
l1 = [1,2,3,('apple','banana','orange'),['喜羊羊','懒羊羊','灰太狼']]
# l2 = l1
# l1.append('666')
# print(l1,id(l1))
# print(l2,id(l2))

# 浅copy:开辟新的内存空间，但里面的元素还是沿用之前的内存地址

# l2 = l1.copy()
# l1.append('666')
# print(l1,id(l1))
# print(l2,id(l2))

l2 = l1.copy()
l1[-1].append('666')

print(l1,id(l1[0]))
print(l2,id(l2[0]))
print(l1,id(l1[-1]))
print(l2,id(l2[-1]))
print(l1,id(l1))
print(l2,id(l2))

# 深copy:开辟新的内存空间，但里面不可变的元素还是沿用之前的内存地址，为可变元素开辟新的内存空间
# import copy

# l2 = copy.deepcopy(l1)
# l1[-1].append('红太狼')
# # l2[0] = 'lemon'

# print(l1,id(l1[0]))
# print(l2,id(l2[0]))
# print(l1,id(l1[-1]))
# print(l2,id(l2[-1]))
# print(l1,id(l1))
# print(l2,id(l2))