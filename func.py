#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :func.py
@Description   :输入M和N计算C(M,N)
@Datatime      :2020/08/14 18:36:56
@Author        :AshJo
@Version       :v1.0
'''
import math
import os
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)

# 把重复的代码逻辑重构成函数

# def factorial(num):
#     result = 1
#     for n in range(1,num + 1):
#         result *= n
#     return result

# m = int(input('m = '))
# n = int(input('n = '))


# print(factorial(m))
# print(factorial(n))
# print(factoria(m) // factorial(n) // factorial(m-n))

# print(math.factorial(m))
# print(math.factorial(n))
# print(math.factorial(m) // math.factorial(n) // math.factorial(m-n))
# print(math.factorial(m) // math.factorial(n) // math.factorial(m-n))


# print(math.factorial(2))
# print(math.factorial(3))



# 函数的参数
# 在Python中，函数的参数可以有默认值，也支持使用可变参数

from random import randint


# 默认参数
def roll_dice(n=2):
    """摇骰子"""
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

# 指定多个默认参数
# def add(a=0,b=0,c=0):
#     """3个数相加"""
#     return a + b + c


# 在参数名前面的*表示args是一个可变参数
# 在调用add函数时可以传入0个或多个参数

def add(*arg):
    """N个数相加"""
    total = 0
    for val in arg:
        total += val
    return total
    

# 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# 摇三颗色子
# print(roll_dice(3))

# 在调用add函数时可以传入0个或多个参数
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))

# 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))


# 练习

def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
    
def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

def meeting(sex,age,area):
    print('打开探探')
    print('进行筛选：性别: %s ,年龄: %s, 地区: %s' % (sex,age,area))
    print('左滑一下')
    print('右滑一下')
    print('找朋友')
    print('悄悄话......约吗？走起！')

# 比较大小参数   三元运算符
def large_num(num1,num2):
    return num1 if num1 > num2 else num2

def str_link(s1,s2):
    return s1+s2


# print(str_link(s2='hello',s1='喜羊羊'))

# print(large_num(15,30))

# meeting('女','22','东莞')

# def func(x):
#     return len(x) > 5
# print(func([1,2,3,4,5,6]))


# register函数：接收四个参数。将四个参数追加到文件中
def register(n,a,e,s='男'): # sex为默认参数
    with open('student.msg',encoding='utf-8',mode='a') as f1:
        f1.write(f'{n}|{s}|{a}|{e}\n')
# 无限循环，用户持续输入：while input
# while True:
#     name = input('请输入姓名(Q或者q退出):')
#     if name.upper() == 'Q':
#         break
#     sex = input('请输入性别:')
#     age = input('请输入年龄:')
#     edu = input('请输入学历:')
#     if sex.strip() == '':
#         register(name,age,edu,s='男')
#     else:
#         register(name,age,edu,sex)


# 调用函数修改源文件，替换文件内容
def filecontent_replace(path,old_content,new_content):
    with open(path,encoding='utf-8') as f1, \
        open(path+'.new',encoding='utf-8',mode='w') as f2:
        for line in f1:
            new_line = line.replace(old_content,new_content)
            f2.write(new_line)
    os.remove(path)
    os.rename(path+'.new',path)
# filecontent_replace('student.msg','女','男')

# 形参角度：
# 万能参数
# *args   约定俗称 *args 不知道传入实参的个数和名称时使用
# * 函数定义时，*代表聚合。将所有的位置参数聚合成一个元组，赋值给args

def eat(*args):
    print(args)
    print("我请你吃：%s %s %s %s %s" % args)
    print(type(args)) # args数据类型为tuple

# eat('桂花糕','北京烤鸭','热干面','兰州拉面','冬瓜鸡')

# 计算传入实参的相加总和
def sum_count(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
# print(sum_count(1,2,3,4,5,6))

# **kwargs 关键字参数
# 函数定义时：** 将所有的关键字参数聚合到一个字典中，并将这个字典赋值给了kwargs 
# def func(**kwargs):
#     print(kwargs)
# func(name='孙悟空',skill='七十二变',figh='金箍棒')

# 仅限关键字参数
# def func(a,b,*args,sex='男',c,**kwargs):
#     print(a,b)
#     print(args)
#     print(sex)
#     print(kwargs)
# func(1,2,3,6,9,c='cat',name='孙悟空',skill='龟派气功')

# * **在用于函数的调用时，*代表打散
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)

# result = func('孙悟空','猪八戒','沙和尚',[11,22,33],**{'k1':'栈'})
# print(result)

# func('abcde',[1,2,3,4,5])
# func(*{'name':'孙悟空'},*{'age':20})
# func(**{'name':'孙悟空'},**{'age':20})

# def wrapper():
#     def innner():
#         print(666)
#     innner()

# wrapper()


# def func1():
#     print('in func1')
# def func2(x):
#     print('in func2')
#     return x
# def func3(y):
#     print('in func3')
#     return y

# # func2(func1)
# ret = func2(func1)  # func1()
# # print(ret)
# ret()
# ret2 = func3(func2) # 
# ret3 = ret2(func1)  # ret2 = func2()
# ret3()      # ret3 = func1()



