#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :tuple.py
@Description   :
@Datatime      :2020/08/15 20:18:51
@Author        :AshJo
@Version       :v1.0
'''

tu = (100,'喜羊羊',True,[1,2,3])

print(tu[0])
print(tu[0:4])

# 查看
for i in tu:
    print(i)
tu[-1].append(4)

#元组中的元素不允许增删改
# tu[0] = '99'

print(len(tu))
print(tu)

# 应用：存放重要数据，不经常修改
# 元组的拆包。分别赋值

a,b = (1,2)
print(a,b)

for i in range(2,101,2):
    print(i)

# 利用for循环，利用range将列表的索引依次打印出来
l1 = [122,'灰太狼',True,'Sindy',True]

for i in range(len(l1)):
    print(i)
