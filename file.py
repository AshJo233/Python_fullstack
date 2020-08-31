#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :file.py
@Description   :
@Datatime      :2020/08/22 11:24:28
@Author        :AshJo
@Version       :v1.0
'''

'''
open内置函数，open底层调用的是操作系统的接口
f1，变量。对文件进行任何的操作，都需要通过文件句柄
encoding:指定编码本,可以不写，使用系统默认的编码集
win:gbk
linux:utf-8
mac:utf-8
f1.close 关闭文件句柄
'''

'''
文件操作三部曲：
1.打开文件
2.对文件句柄进行操作
3.关闭文件
'''

# 文件操作

#f1 = open('D:\少妇白洁.txt',encoding='utf-8',mode='r')


# 文件操作的读
# mode:r(读纯文本),rb(用于读取非文本文件，比如图片或视频音频等)

# content = f1.read()
# l1 = f1.readline()

# l2 = f1.readlines()
# for line in l2:
#     print(line)
# print(content)
# print(l1)
# print(l2)
# f1.close()

# 文件操作的写 mode: w,wb
# 机制：没有文件就创建然后写入，存在文件则清空原内容，对文件写入覆盖

# f2 = open('D:\少妇白洁.txt',encoding='utf-8',mode='w')
# f2.write('写点啥呢？')
# f2.close()


# 文件操作的追加 mode: w,wb
# 机制：没有文件就创建然后写入，存在文件则直接在源文件上写入追加的内容

# f2 = open('D:\少妇白洁.txt',encoding='utf-8',mode='a')
# f2.write('\n恭喜发财！')
# f2.close()

# tell() seek() 返回和控制光标位置

# f3 = open('D:\少妇白洁.txt',encoding='utf-8',mode='r')
# print(f3.seek(6))
# print(f3.tell())
# content = f3.read()
# print(content)
# f3.close()

# 文件的修改

# with open('D:\少妇白洁.txt',encoding='utf-8',mode='r') as f1 \
#     open('D:\精神小伙.txt',encoding='utf-8',mode='w') as f2:
    
#     for line in f1:
#         print(line)