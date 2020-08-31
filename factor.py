#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :factor.py
@Description   :输入两个正整数计算它们的最大公约数和最小公倍数
@Datatime      :2020/08/07 21:31:30
@Author        :AshJo
@Version       :v1.0
'''

x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较大的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
