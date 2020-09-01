#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :my_module.py
@Description   :自定义模块
@Datatime      :2020/09/02 20:30:48
@Author        :AshJo
@Version       :v1.0
'''

age = 6

def f1():
    age = 3
    print(f'可爱不是{age}岁')

def main():
    print(age)
    f1()

if __name__ == '__main__':
    main()
    
