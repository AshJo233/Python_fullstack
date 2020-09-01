#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :blog_login.py
@Description   :
@Datatime      :2020/09/01 21:40:23
@Author        :AshJo
@Version       :v1.0
'''

# 大作业：使用装饰器模拟博客园登录

status_dict = {
    'username': None,
    'password': None,
    'status': False,
}

# 获取文件转换成字典
def get_user_pwd():
    user_dict = {}
    with open('day14\\register',encoding='utf-8') as f:
        for line in f:
            line_list = line.strip().split('|')
            user_dict[line_list[0].strip()] = line_list[1].strip()
    return user_dict

def login():
    u_dict = get_user_pwd()
    count = 1
    while count < 4:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username in u_dict and password == u_dict[username]:
            print('登录成功！')
            status_dict['username'] = username
            status_dict['password'] = password
            status_dict['status'] = True
            print(status_dict)
            return True
        else:
            print('登录失败！请检查用户名或密码')
        count += 1
    if count >= 4:
        print('尝试次数太多，稍后再试吧......')
        return False

def register():
    username = input('请输入新注册用户名：').strip()
    password = input(f'请输入新注册用户{username}的密码：').strip()
    with open('day14\\register',encoding='utf-8',mode='a') as f:
        f.write('\n')
        f.write(username+'|'+password)
    print('注册成功！')
    return True

def auth(f):
    '''
    装饰器完成：访问装饰器函数之前，写一个三次登录认证的功能。
    登录成功：让其访问被装饰的函数，登录没有成功，不让访问。
    :param f
    :return
    '''
    def inner(*args,**kwargs):
        '''访问函数之前的操作，功能'''
        if status_dict['status']:
            ret = f(*args,**kwargs)
            '''访问函数之后的操作，功能'''
            return ret
        else:
            while True:
                choose = input('注册(1) or 登录(2)：')
                if choose == '1':
                   ret1 = register()
                elif choose == '2':
                    ret2 = login()
                    if ret2 == True:
                        ret = f(*args,**kwargs)
                        return ret
                        break
                else:
                    continue
    return inner


@auth
def article():
    print('欢迎访问文章页面！')

@auth    
def comment():
    print('欢迎访问评论页面！')

@auth    
def dariy():
    print('欢迎访问日记页面！')

article()
comment()
dariy()
