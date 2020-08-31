# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# '''
# @Filename      :dict.py
# @Description   :
# @Datatime      :2020/08/16 16:37:30
# @Author        :AshJo
# @Version       :v1.0
# '''

# # 字典的创建 多种方式
# dic = dict({'name':'AshJo', 'age':22, 'sex':1})
# print(dic)

# # 字典的操作

# # 增
# dic['hobby'] = ['唱','跳','rap','篮球']
# dic.setdefault('work','teacher')
# print(dic)

# # 删 pop()有返回值

# # 字典里 删除判断输出
# # res = dic.pop('sex',None)
# # print(res)
# # print(dic)

# # 改
# dic['age'] = 23
# print(dic)

# # 查
# print(dic.get('hobby',None))

# # 遍历key
# for key in dic.keys():
#     print(key)

# print(dic.keys())

# # 遍历value
# for value in dic.values():
#     print(value)

# print(list(dic.values()))

# # items()
# print(dic.items())
# for key,value in (dic.items()):
#     print(key,value)

# # 面试题：一行代码变量值互换

# a = 1
# b = 2
# a,b = b,a
# print(a,b)

# # 字典练习
# dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}
# dic.setdefault('k4','v4')
# dic['k1'] = 'alex'
# dic['k3'].append(44)
# dic['k3'].insert(0,18)
# print(dic)

# # 字典嵌套

# dic = {
#     'name': '灰太狼',
#     'age': 30,
#     'wife': [{'name':'红太狼','age':33,'hobby':'煮饭'}],
#     'children': {'boy':'小灰灰','girl':'小红红'}
# }

# print(dic)
# print(dic['name'])
# print(dic['wife'][0])
# print(dic['wife'][0]['name'])
# print(dic['children']['girl'])



# dic1 = {
#     'name': ['alex',2,3,5],
#     'job': 'teacher',
#     'oldboy': {'alex':['python1','python2',100]}
# }

# dic1['name'].append('wusir')
# dic1['name'][0] = dic1['name'][0].upper()
# dic1['oldboy'].setdefault('老男孩','linux')
# dic1['oldboy']['alex'].remove('python2')

# print(dic1)


