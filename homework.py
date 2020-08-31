#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :homework.py
@Description   :
@Datatime      :2020/08/20 16:31:24
@Author        :AshJo
@Version       :v1.0
'''

# 选择商品列表1
# goods = [
#     {"name": "Macbook", "price": 12999},
#     {"name": "iphoneX", "price": 8999},
#     {"name": "switch", "price": 5999},
#     {"name": "x-box", "price": 3999},
# ]

# # count = 1
# # for i in goods:
# #     print(count,i['name'],i['price'])
# #     count += 1

# # for index in range(len(goods)):
# #     print(index+1,goods[index]['name'],goods[index]['price'])

# while True:
#     for num,dic in enumerate(goods):
#         print("{}\t{}\t{}".format(num+1,dic['name'],dic['price']))
#     choice_num = input("Please input a goods number('q' or 'Q' to exit'):").strip()
#     if choice_num.isdecimal():
#         choice_num = int(choice_num)
#         if 0 < choice_num <= len(goods):
#             print("你输入的商品为{},价格为{}".format(goods[choice_num-1]['name'],goods[choice_num-1]['price']))
#         else:
#             print("选择数字超出范围，请重新输入！")
#     elif choice_num.upper() == 'Q':
#         print("Bye!")
#         break
#     else:
#         print("输入数据格式有误，请重新输入！")



# v1 = [1,2,3,4,5,6,7,8,9]
# v2 = {}

# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item,]
# print(v2)

# 车牌区域划分，给下列车牌，根据车牌的信息，分析各省的车牌持有量
cars = ['鲁A32444','粤757626','鲁B12333','京B898M','黑C46555','湘C78568','沪B25041','鄂A88888']
local = {'沪':'上海','黑':'黑龙江','鲁':'山东','鄂':'湖北','粤':'广东','京':'北京','湘':'湖南'}
dic = {}

# 遍历循环体cars
# 在循环中给字典添加键值对
# 判断字典中的键值对，没有的话则创建新的，有的键则统计+1
# for i in cars:
#     dic[local[i[0]]] = dic.get(local[i[0]],0) + 1
# print(dic)



# 计算乘阶

def cj(arg):
    count = 1
    for i in range(arg,1,-1):
        count *= i
    print(count)
cj(10)