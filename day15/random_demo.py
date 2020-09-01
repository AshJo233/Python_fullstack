#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :random_demo.py
@Description   :radom模块的演示
@Datatime      :2020/09/03 13:55:57
@Author        :AshJo
@Version       :v1.0
'''

import random

# 获取[0.0,1.0]范围内的浮点数
print(random.random()) 

# 获取[a,b]范围内的一个浮点数

print(random.uniform(3,5))

# 获取[a,b]范围内的一个整数
print(random.randint(6,10))

# 把参数指定的数据中的元素打乱。参数必须是一个可变的数据类型 (返回值是None)
lst = list(range(10))
# print(random.shuffle(lst))
random.shuffle(lst)
print(lst)

# 从x中随机抽取k个数据，组成一个列表返回。
print(random.sample(lst,5))
