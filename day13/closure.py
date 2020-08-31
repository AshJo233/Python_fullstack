#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :closure.py
@Description   :
@Datatime      :2020/08/31 13:41:23
@Author        :AshJo
@Version       :v1.0
'''

# 封闭的东西：保证数据安全


# 方案一：

# 全局变量，数据不安全
l1 = [] 


# 计算平均收盘价
# def make_averager(new_value):
#     l1.append(new_value)
#     total = sum(l1)
#     averager = total / len(l1)
#     return averager

# print(make_averager(100000))
# print(make_averager(200000))
# print(make_averager(205000))


# 方案二：使用闭包

def make_averager():
    l1 = []
    def averager(new_value):
        l1.append(new_value)
        total = sum(l1)
        return  total / len(l1)
    return averager

avg = make_averager()
print(avg(100000))
print(avg(110000))
print(avg(160000))

# 判断闭包，输出自由变量
print(avg.__code__.co_freevars)
'''
闭包：
内层函数对外层函数非全局变量进行调用和使用，就会形成闭包。
被引用的非全局变量也称作自由变量，这个自由变量会与内层函数产生一个绑定关系，
自由变量在内存中不会消失
'''