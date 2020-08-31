#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :homework.py
@Description   :
@Datatime      :2020/08/30 11:33:48
@Author        :AshJo
@Version       :v1.0
'''


# 列表推导式

# 过滤长度小于3的字符串列表，并将剩下的转换成大写
l1 = ['apple','grape','watermelon','lenmon','egg','sx','rush','qq']

# res = [i.upper() for i in l1 if len(i) > 3]
# print(res)


# 使用yield from 简化 yield
# def chain(*args):
#     for it in args:
#         for i in it:
#             yield i
# def chain(*args):
#     for it in args:
#         yield from it

# g = chain('abc',[1,2,3])
#迭代器转换成列表
# print(list(g))


# 构建一个列表，列表里面有四种不同尺寸的衣服，每个尺寸都有两种颜色
# l1 = []
colors = ['black','white']
sizes = ['S','M','L','XL']
# for color in colors:
#     for size in sizes:
#         l1.append((color,size))
# l1 = [(color,size) for color in colors for size in sizes]
# print(l1)


# 结果再取余2
# v = [i % 2 for i in range(10)]

# 生成器表达式，不会直接输出值
# v = (i % 2 for i in range(10))
# print(v)


# 看代码求结果（面试题）
# def demo():
#     for i in range(4):
#         yield i

# g = demo()

# g1 = (i for i in g)
# g2 = (i for i in g1)

# print(list(g1))
# print(list(g2))


# 看代码求结果：（面试题）

def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g = test()
for n in [1,10]:
    g = (add(n,i) for i in g)

# 1.g=(add(1,0)) 2. g=(add(10,1))

# print(list(g))  # [1,11]



# 修改筛选列表的值，默认为索引的循环，反向取值，不改变索引
alist = [2,4,5,6,7]
for i in range(len(alist)-1,-1,-1):
    if alist[i] % 2 == 0:
        alist.pop(i)
print(alist)
