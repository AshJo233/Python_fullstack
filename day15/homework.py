#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :homework.py
@Description   :
@Datatime      :2020/09/02 14:16:35
@Author        :AshJo
@Version       :v1.0
'''


# 实现一个装饰器，通过一次调用使函数执行5次

# def wrapper(f):
#     # f = func
#     def inner(*args,**kwargs):
#         for i in range(5):
#             ret = f(*args,**kwargs)
#         return ret
#     return inner

# @wrapper # func = wrapper(func)
# def func():
#     print('in func')
# func()



# 实现一个装饰器，每次调用函数时，将函数以及函数的时间节点写入文件

import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))

def wrapper(f):
    def inner(*args,**kwargs):
        with open('day15\\log',encoding='utf-8',mode='a') as f1:
            struct_time = time.localtime()
            f1.write(f'北京时间{time.strftime("%Y-%m-%d %H:%M:%S",struct_time)} 执行了{f.__name__}函数\n')
        ret = f(*args,**kwargs)
        return ret
    return inner

@wrapper
def func():
    print('in func')

func()
time.sleep(1)
func()
time.sleep(2)
func()
time.sleep(3)
func()