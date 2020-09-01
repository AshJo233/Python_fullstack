#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :decorators.py
@Description   :
@Datatime      :2020/09/01 14:17:12
@Author        :AshJo
@Version       :v1.0
'''

# 装饰器

#* 在不改变原函数的代码以及调用方式的前提下，为其增加新的功能
#* 完全遵守开放封闭原则


# 不能改变原函数的调用方式

import time

# timmer()装饰器
def timmer(f):
    def inner(*args,**kwargs):
        start_time = time.time()
        r = f(*args,**kwargs)
        end_time = time.time()
        print(f'测试该函数的执行效率：{end_time-start_time}')
        return r
    return inner

@timmer # 装饰器语法糖
def login(name):
    '''省略的代码集......'''
    time.sleep(2)   # 模拟的网络延迟或测试代码效率
    print(f'欢迎{name}登录博客园首页！')
    return True  

@timmer
def dariy(name,age):
    '''省略的代码集......'''
    time.sleep(3)   # 模拟的网络延迟或测试代码效率
    print(f'欢迎{age}岁的{name}登录日志页面！')
    return 666

login('AshJo')
ret = login('AshJo')
print(ret)

dariy('AshJo',18)
ret = dariy('AshJo',18)
print(ret)


## 标准的装饰器结构：

def wrapper(f):
    def innner(*args,**kwargs):
        '''添加额外的功能：执行被装饰函数之前的操作'''
        ret = f(*args,**kwargs)
        '''添加额外的功能：执行被装饰函数之后的操作'''
        return ret
    return innner