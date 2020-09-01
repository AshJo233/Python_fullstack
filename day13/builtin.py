#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :builtin.py
@Description   :
@Datatime      :2020/08/30 11:50:17
@Author        :AshJo
@Version       :v1.0
'''

# eval()

# help()

# callable() 判断一个对象是否能被调用

# int()

# float()

# complex()


# 进制转换(bin,oct,hex)


# divmod(10,3) 算商取余



# round() 保留浮点数的小数位数

# min()返回字典中最小值的键
dic = {'a':1, 'b':2, 'c':3}
print(min(dic,key=lambda arg: dic[arg]))


# 返回l2列表中各个元组中int值最小的字符串元素
l2 = [('喜羊羊',18),('懒羊羊',16),('灰太狼',35),('小灰灰',3)]
print(min(l2,key=lambda arg: arg[1])[0])


# max()

# sorted() 排序函数
print(sorted(l2,key=lambda arg: arg[1],reverse=True))


# map() 

# filter() 列表推导式的筛选


# sum() 求和

# reduce()