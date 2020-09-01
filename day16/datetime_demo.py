#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :datetime_demo.py
@Description   :日期时间模块
@Datatime      :2020/09/06 12:44:04
@Author        :AshJo
@Version       :v1.0
'''

import datetime

# date类
d = datetime.date(2020,9,6)
print(d,type(d))
print(d.year)
print(d.month)
print(d.day)


# time类
t = datetime.time(12,52,59)
print(t,type(t))
print(t.hour)
print(t.minute)
print(t.second)

# datetime类
dt = datetime.datetime(2020,11,11,11,11,59)
# print(dt,type(dt))

# datetime中的类主要用于数学运算
# timedelta类：时间变化量
# 创建时间对象
# dtd = datetime.timedelta(days=1)
# print(dtd,type(dtd))

# res = d + dtd
# print(res,type(res))

# 时间变化量的运算是否会产生进位
dtd = datetime.timedelta(seconds=3)
print(dtd,type(dtd))

res = dt + dtd
print(res,type(res))

# 练习：
# 结合使用datetime模块，快捷判断闰年和平年
year = int(input('输入年份：'))
d1 = datetime.datetime(year,3,1)
d2 = datetime.timedelta(days=1)
cd = d1 - d2
# print(cd.day)
if cd.day == 29:
    print(f'{year}是闰年')
else:
    print(f'{year}是平年')

