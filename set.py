#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :set.py
@Description   :
@Datatime      :2020/08/20 13:24:55
@Author        :AshJo
@Version       :v1.0
'''

# 集合的创建

set1 = set({True,1,3,"喜羊羊",1,2,3,'4',5,'6','灰太狼',False,('apple','banana','orange')})
print(set1)

# 空集合
# print({},type({})) # 空字典
# set2 = set()
# print(set2,type(set2))



# 集合的有效性测试
'''
集合中的元素必须是可哈希(hashable)的数据类型（即不可变数据结构）
作用：
它是一个将大体量数据转化为很小数据的过程，甚至可以仅仅是一个数字，以便我们可以用在固定的时间复杂度下查询它，
所以，哈希对高效的算法和数据结构很重要。
同理：不可哈希的数据类型，即可变的数据结构 (字典dict，列表list，集合set)
'''

# set3 = set({[1,2,3],78,{'name':'喜羊羊'}})
# print(set3)

# 增：
set1.add('你xx')
print(set1)

# update：迭代地增加
set1.update('abcd')
print(set1)

# 删 remove(按照元素删除)
# pop()随机删除
# set1.remove('你xx')
# print(set1)
# set1.pop()
# print(set1)

# 集合不可以直接改
# set1['喜羊羊'] = set1['懒洋洋']
# print(set1)

# 变相修改,先删后增
set1.remove('喜羊羊')
set1.add('懒羊羊')
print(set1)


set5 = ({1,2,3,4,5})
set6 = ({4,5,6,7,8})
set7 = ({1,2,3})
# 交集
print(set5 & set6)

# 并集
print(set5 | set6)

# 差集
print(set5 - set6)
print(set6 - set5)

# 反交集
print(set5 ^ set6)

# 子集
print(set7 < set5)

# 超集
print(set5 > set7)

# * 利用集合的特性，实现列表的去重（由于输出是无序的，列表的索引会改变）
# l1 = [1,1,2,2,3,3,4,4,5,5,'a','a','b','b','c','c','灰太狼','灰太狼']
# print(list(set(l1)))

list3 = ["a","a","a","b","b","c","d","d","f",'f','G','G','g','g']
#list3.reverse()  # 先反转列表，从后往前删
for i in list3:    # 外层循环控制每次需要判定的元素
    for _ in range(list3.count(i)):    # 内层循环控制每次执行删除元素的次数，循环多次就彻底删除。
        if list3.count(i) > 1:
            list3.remove(i)    # 如果该元素个数大于1，则执行删除操作
#list3.reverse()      # 最后再反转列表，保证第一次出现的元素顺位保留下来
print(list3)