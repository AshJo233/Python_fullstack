#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :sys_demo.py
@Description   :和python解释器相关的操作
@Datatime      :2020/09/06 14:28:13
@Author        :AshJo
@Version       :v1.0
'''

import sys

# 获取命令行方式运行的脚本后面的参数
print('脚本名：',sys.argv[0])
print('第一个参数：',sys.argv[1])
print('第二个参数：',sys.argv[2])
# print(type(sys.argv[1])) # <class 'str'>

arg1 = sys.argv[1]
arg2 = sys.argv[2]
print(arg1+ ' ' +arg2+ '!')

# 查看已加载的模块
print(sys.modules)