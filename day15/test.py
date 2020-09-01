#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :test.py
@Description   :
@Datatime      :2020/09/02 19:57:08
@Author        :AshJo
@Version       :v1.0
'''

# def func():
#     print('hello world')

# def main():
#     a = 1
#     print(a)

#     for i in range(4):
#         print(i)

#     func()

# a = 1
# print(a)

# for i in range(4):
#     print(i)

# func()

# if __name__ == '__main__':
#     main()



# name = '喜羊羊'
# def func():
#     global name
#     name = '灰太狼'
# print(name)
# func()
# print(name)


# def func():
#     name = '喜羊羊'
#     def inner():
#         nonlocal name
#         name = '灰太狼'
#     print(name)
#     inner()
#     print(name)
# func()


# 整数加法器

# content = input("输入：")
# # print(content.split('+'))
# sum = 0
# for i in content.strip().split('+'):
#     print(i)
#     sum += int(i)
# print(sum)


# 最佳电影投票

lst = ['肖申克的救赎','霸王别姬','盗梦空间','阿凡达','阿甘正传','猫鼠游戏']
dic = {'肖申克的救赎': 0,'霸王别姬': 0,'盗梦空间': 0,'阿凡达': 0,'阿甘正传': 0,'猫鼠游戏': 0}

dic1 = {}
while True:
    for index,movie_name in enumerate(lst):
        print(f'序号：{index+1} 电影名称：{movie_name}')
    num = input("请输入您投票的电影序号：").strip()
    if num.isdecimal():
        num = int(num)
        if 0 < num <= len(lst):
            if lst[num-1] not in dic1:
                    dic1[lst[num-1]] = 1
                    print(dic1)
            else:
                    dic1[lst[num-1]] += 1
                    print(dic1)
        else:
            print('输入超出提供的序号范围，请重新输入!')
    elif num.upper() == 'Q':
        break
    else:
        print('输入的投票数据格式有误，请重新输入!')
for movie_name,count in dic1.items():
    print(f'电影 《{movie_name}》 的最终投票结果为：{count}')