#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :iter.py
@Description   :
@Datatime      :2020/08/27 14:37:20
@Author        :AshJo
@Version       :v1.0
'''


s1 = 'apple'
l1 = [1,2,3]
d1 = {'name':'jojo','age':18}
# print('__iter__' in dir(s1))
# print('__iter__' in dir(d1))
# print('__iter__' in dir(range(10)))

# 将可迭代对象转换为迭代器对象
# obj = iter(l1)
# print(obj,type(obj))
# for i in range(3):
#     print(next(obj))



# 利用while循环模拟for循环对（可迭代对象）进行取值的机制

l1 = [i for i in range(101)]
obj = iter(l1)
print(obj)
# while True:
#     try:
#         print(next(obj))
#     except StopIteration:
#         break
