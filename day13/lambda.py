#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :lambda.py
@Description   :
@Datatime      :2020/08/30 11:33:42
@Author        :AshJo
@Version       :v1.0
'''

# 匿名函数：一句话函数，比较简单的函数
def func(a,b):
    return a + b

# 构建匿名函数  
func1 = lambda a,b: a + b
print(func1(1,2))

# 接收一个可切片的数据，返回索引为0和2的对应元素（元组形式）
func2 = lambda a: (a[0],a[2])
print(func2([1,2,3,4]))

# 写匿名函数：接收两个int参数，将较大的数据返回
func3 = lambda x,y: x if x > y else y
print(func3(100,99))