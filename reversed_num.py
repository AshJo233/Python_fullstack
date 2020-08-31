#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :reversed_num.py
@Description   :正整数反转
@Datatime      :2020/08/09 15:21:21
@Author        :AshJo
@Version       :v1.0123
'''
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)