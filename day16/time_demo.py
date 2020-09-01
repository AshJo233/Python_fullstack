#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :time_demo.py
@Description   :time 模块
@Datatime      :2020/09/04 19:00:49
@Author        :AshJo
@Version       :v1.0
'''

import time

# 获取时间戳
# 时间戳：从时间元年(1970-01-01 00:00:00)到现在经过的秒数。
print(type(time.time()))
# print(type(time.localtime()))
# print(type(time.strftime('%Y-%m-%d %H:%M:%S')))

# 获取格式化时间对象(由九个字段组成)
# 默认参数为当前系统的时间戳（参数：距离时间元年过xx秒）
print(time.gmtime())  # GMT：格林时间
print(time.gmtime(1))
print(time.localtime()) # GMT：格林时间 + 8 hours 【东八区】

# 格式化时间对象和字符串之间的转换
s = time.strftime('%Y-%m-%d %H:%M:%S')
print('北京时间：'+s)

time_obj = time.strptime('2020-09-04 19:59:42','%Y-%m-%d %H:%M:%S')
print(time_obj)


# 暂停程序，睡眠xx秒（应对反爬机制）
for i in range(5):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)