#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :homework.py
@Description   :
@Datatime      :2020/09/01 12:42:22
@Author        :AshJo
@Version       :v1.0
'''


# 用map来处理字符串列表，把列表中所有人都变成sb，比方alex_sb
name = ['oldboy','alex','wusir']
# print([n + '_sb' for n in name])
print(list(map(lambda x: x + '_sb', name)))


# 用map来处理下述，然后用list得到一个新的列表，列表每个人的名字都是sb结尾
l = [{'name':'alex'},{'name':'y'}]
print(list(map(lambda x: x['name'] + 'sb',l)))


# 使用zip()+filter()合并以及过滤列表数据
l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天','嘻哈']
tu = ['**','***','****','*****','******','*******']

print(list(filter(lambda x: x[0] > 2 and len(x[-1]) >= 4,zip(l1,l2,tu))))

# 求结果（面试题）
v = [lambda :x for x in range(10)]
print(v)
print(v[0])
print(v[0]())



def num():
    return [lambda x: i*x for i in range(4)]
print([m(2) for m in num()])


# 实现模拟三次用户登录的功能

# 获取文件转换成字典
def get_user_pwd():
    user_dict = {}
    with open('day14\\register',encoding='utf-8') as f:
        for line in f:
            line_list = line.strip().split('|')
            user_dict[line_list[0].strip()] = line_list[1].strip()
    return user_dict

# 登录功能
def login():
    u_dict = get_user_pwd()
    count = 1
    while count < 4:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username in u_dict and password == u_dict[username]:
            print('登录成功！')
            return True
        else:
            print('登录失败！请检查用户名或密码')
        count += 1

# 调用
if __name__ == '__main__':
    login()
