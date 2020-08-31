#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :list.py
@Description   :
@Datatime      :2020/08/14 21:09:00
@Author        :AshJo
@Version       :v1.0
'''

# li = [100,'喜羊羊',True,[1,2,3]]
# # 索引
# print(li[0],type(li[0]))
# print(li[1],type(li[1]))
# # 切片
# print(li[0:3])
# li = [1,3,2,'a',4,'b',5,"c"]

# l1 = li[0:3]
# print(l1)

# l2 = li[3:6]
# print(l2)

# l3 = li[1:-2:2]
# print(l3)

# l4 = li[-3:0:-2]
# print(l4)

# 列表的创建
# 方式一：
# l1 = [122,'灰太狼',True]
# print(l1[-1],type(l1[-1]))

# 方式二：
# l1 = list()
# l1 = list('sfkjsdlfjsdlkkfjsdklj')
# print(l1)

# 方式三：列表推导式



# 增删改查

# l1 = [122,'灰太狼',True,'Sindy',True]

# 直接追加
# l1.append('喜羊羊')

# 迭代追加
# l1.extend([1,6]) 

# 插入
# l1.insert(1,'1931')

# 删除 

# pop()按索引删除，默认会删除最后一个列表元素，返回删除的值
# l1.pop(1)
# print(l1.pop())
# print(l1)

# remove()指定元素删除，有重复元素则删除左边第一个出现的元素
# l1.remove(122)
# l1.remove(True)
# print(l1)

# 清空列表所有元素
# l1.clear

# del (索引删除)
# del l1[0:2]
# print(l1)

# 反向倒序
# l1.reverse()
# print(l1)

# 按切片修改
# l1[1::] = 'abcde'
# print(l1)

# while True:
#     name = input("Please input name for append to l1('Q'or'q' to exit):")
#     if name.upper() == 'Q':
#         break
#     l1.append(name)
# print(l1)



# 练习
# li = ["alex",'WuSir','ritian','barry','wenzhou']
# print(len(li))
# li.append("seven")
# print(li)
# li.insert(1,'Tony')
# print(li)
# li.insert(2,'Kelly')
# print(li)
# l2 = [1,'a',3,4,'heart']
# li = li + l2
# print(li)
# s = 'qwert'
# li = li + list(s)
# print(li)
# li.remove('ritian')
# print(li)
# print(li.pop(1))
# print(li)
# del li[1:4]
# print(li)

# 列表的嵌套

# l1 = [1,2,'taibai',[1,'alex',3]]
# l1[2] = l1[2].upper()
# # print(s1)
# print(l1)

# l1[-1].append("老男孩教育")
# print(l1)

# l1[-1][1] += 'sb'
# print(l1)

# 列表嵌套练习

# lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3 , "1"]], 89], "ab", "adv"]

# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)

# lis[3][2][1][1] = "100"
# print(lis)
# print(type(lis[3][2][1][1]))

# lis[3][2][1][2] = 101
# print(lis)
# print(type(lis[3][2][1][2]))


# 面试题：
# l1 = range(5)
# print(l1)
# print(l1[-1])

# for i in range(5,1,-1):
#     print(i)


# # 整数加数器
# content = input("请输入内容：")
# # print(content)
# l1 = content.split('+')
# # print(l1)

# result = 0
# for i in range(len(l1)):
#     result += int(l1[i].strip()) 
# print(result)


# 计算用户输入内容中有多少个整数(以个数为单位)
# content = input("请输入内容：")
# # # print(content)
# l1 = list(content)
# count = 0
# for i in l1:
#     if i.isdecimal() is True:
#         count += 1
# print(count)

# 判断字符串回文 例如：上海自来水来自海上


# content = input("请输入内容：")
# # for i in content:
# # print(content)
# # print(content[::-1])
# if content == content[::-1]:
#     print("yes")
# else:
#     print('no')


# 敏感词汇列表
# l1 = ['共产党','斯大林','世界大战','苍老师','傻逼']
# l2 = []
# comment = input("请输入评论：")
# for word in l1:
#     if word in comment:
#         comment = comment.replace(word,'*' * len(word))

# print(comment)
# l2.append(comment)
# print(l2)

# l1 = [2, 30, "k", ["qwe", 20, 89], "ab", "adv"]

# for i in l1:
#     if type(i) == list:
#         for j in i:
#             print(j)
#     else:
#         print(i)


# print(l1)

# result = 0
# for i in range(len(l1)):
#     result += int(l1[i].strip()) 
# print(result)


# 作业

# users = ['灰太狼','喜羊羊', 666, True, '懒羊羊']
# s = ''
# for i in users:
#     s += str(i) + '_'
# print(s[0:-1])

# s = '_'.join(users)
# print(s)

'''
有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1, 'k1':2......}
'''
# msg = "k : 1 | k1:2 |k2 :3 |k3 :4 "
# dic = {}

# l1 = msg.strip().split('|')
# for i in l1:
#     key,value = i.strip().split(':')
#     dic.setdefault(key.strip(),int(value))
# print(dic)


# 去除列表里的元素，开头为‘周’的字符串
# lst = ['周星星','周大福','太上老君','神奇女侠','周淑怡']
# print(len(lst))
# for i in range(len(lst)-1,-1,-1):
#     if lst[i].strip()[0] == '周':
#         lst.pop(i)
# print(lst)