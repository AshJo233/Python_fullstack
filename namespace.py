#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :namespace.py
@Description   :
@Datatime      :2020/08/26 13:43:28
@Author        :AshJo
@Version       :v1.0
'''

# 命名空间；名称空间

# 全局命名空间；全局名称空间
a = 1
b = 2
def func1():
    f = 5  #局部命名空间，临时名称空间，函数执行结束后就会消失
    # a = 4
    print(f)
    print(a)    # 取值顺序：就近原则（从局部找时） 局部命名空间->全局命名空间->内置命名空间
    print(666)


func1()
c = 3

# 内置命名空间 存放python自带的函数
# 加载顺序：内置命名空间->全局命名空间->局部命名空间



# 作用域：
# 两个作用域
    # 全局作用域：内置命名空间 全局命名空间
    # 局部作用域：局部命名空间

# 局部可以调用上层命名空间的值，但不能修改