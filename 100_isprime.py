#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :100_isprime.py
@Description   :输出一百以内的所有素数
@Datatime      :2020/08/09 16:53:13
@Author        :AshJo
@Version       :v1.0
'''
'''
输入一个正整数判断它是不是素数
提示：素数指的是只能被1和自身整除的大于1的整数。
'''

from math import sqrt

num = 0
while num <= 100:
    is_prime = True
    end = int(sqrt(num))
    for x in range(2,end+1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        print("%d is a Prime number" % num)
    num += 1




