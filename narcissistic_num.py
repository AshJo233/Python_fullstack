#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :narcissistic_num.py
@Description   :找出所有水仙花数
@Datatime      :2020/08/09 15:07:21
@Author        :AshJo
@Version       :v1.0
说明:
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
'''
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# num = input("输入一个三位数：")
# count = 0
# if num.isdecimal():
#     for i in num:
#         count += int(i) ** 3
#     if count == int(num):
#         print("是水仙花数")
#     else:
#         print("不是水仙花数")
# else:
#     print('输入有误')