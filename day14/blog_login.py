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

# 【version 1】

# status_dict = {
#     'username': None,
#     'password': None,
#     'status': False,
# }

# # 获取文件转换成字典
# def get_user_pwd():
#     user_dict = {}
#     with open('day14\\register',encoding='utf-8') as f:
#         for line in f:
#             line_list = line.strip().split('|')
#             user_dict[line_list[0].strip()] = line_list[1].strip()
#     return user_dict

# def login():
#     u_dict = get_user_pwd()
#     count = 1
#     while count < 4:
#         username = input('请输入用户名：').strip()
#         password = input('请输入密码：').strip()
#         if username in u_dict and password == u_dict[username]:
#             print('登录成功！')
#             status_dict['username'] = username
#             status_dict['password'] = password
#             status_dict['status'] = True
#             print(status_dict)
#             return True
#         else:
#             print('登录失败！请检查用户名或密码')
#         count += 1
#     if count >= 4:
#         print('尝试次数太多，稍后再试吧......')
#         return False

# def register():
#     username = input('请输入新注册用户名：').strip()
#     password = input(f'请输入新注册用户{username}的密码：').strip()
#     with open('day14\\register',encoding='utf-8',mode='a') as f:
#         f.write('\n')
#         f.write(username+'|'+password)
#     print('注册成功！')
#     return True

# def auth(f):
#     '''
#     装饰器完成：访问装饰器函数之前，写一个三次登录认证的功能。
#     登录成功：让其访问被装饰的函数，登录没有成功，不让访问。
#     :param f
#     :return
#     '''
#     def inner(*args,**kwargs):
#         '''访问函数之前的操作，功能'''
#         if status_dict['status']:
#             ret = f(*args,**kwargs)
#             '''访问函数之后的操作，功能'''
#             return ret
#         else:
#             while True:
#                 choose = input('注册(1) or 登录(2)：')
#                 if choose == '1':
#                    ret1 = register()
#                 elif choose == '2':
#                     ret2 = login()
#                     if ret2 == True:
#                         ret = f(*args,**kwargs)
#                         return ret
#                         break
#                 else:
#                     continue
#     return inner


# @auth
# def article():
#     print('欢迎访问文章页面！')

# @auth    
# def comment():
#     print('欢迎访问评论页面！')

# @auth    
# def dariy():
#     print('欢迎访问日记页面！')

# article()
# comment()
# dariy()



# 【version 2】

import os

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

# 获取文件转换成列表（用户名）
def get_user_name():
    name_list = []
    with open('day14\\register',encoding='utf-8') as f:
        for i in f.readlines():
            name_list.append(i.split('|')[0])
    return name_list

# 登录
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
        print('尝试登录次数太多，稍后再试吧......')
        return False

# 注册
def register():
    name_list = get_user_name()
    while True:
        username = input('请输入新注册用户名：').strip()
        password = input(f'请输入新注册用户{username}的密码：').strip()
        if username.isalnum():
            if username not in name_list:
                if 5 <= len(password) <= 13:
                    with open('day14\\register',encoding='utf-8',mode='a') as f:
                        f.write('\n')
                        f.write(username+'|'+password)
                    print('注册成功！')
                    return True
                else:
                    print('密码长度不符合规范(6-14位)!')
                    continue
            else:
                print('注册的用户名已存在!')
                continue
        else:
            print('注册的用户名格式不对!')
            continue

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
                choose = input('【注册(1) or 登录(2)】：')
                if choose == '1':
                   ret1 = register()
                elif choose == '2':
                    ret2 = login()
                    if ret2 == True:
                        ret = f(*args,**kwargs)
                        return ret
                        break
                elif choose.upper() == 'Q':
                    break
                else:
                    continue
    return inner

# 文章模块
@auth
def article():
    username = status_dict['username']
    print(f'欢迎{username}进入文章页面！')
    choose = input('1.直接写入内容 or 2.导入md文件').strip()
    if choose.isdecimal():
        choose = int(choose)
        if choose == 1:
            print('请输入文章内容：如【文章标题|xxxxxxxx.......】')
            content = input('开始输入：')
            title = content.strip().split('|')[0]
            doc = content.strip().split('|')[1]
            with open(f'day14\\article\\{title}.text',encoding='utf-8',mode='a+') as f1:
                f1.write(doc)
                print('文件写入完毕')
                return True
        elif choose == 2:
            print('请输入导入md文件路径：如【xxxxxxxx.md】')
            content = input('开始输入：')
            import_file = content.strip()
            title = content.strip().split('\\')[-1].split('.')[0]
            with open(f'{import_file}',encoding='utf-8',mode='r') as f2:
                f2_contect = f2.read()
            with open(f'day14\\article\\{title}.text',encoding='utf-8',mode='a+') as f3:
                f3.write(f2_contect)
                print('导入md文件，成功!')
                return True
        else:
            print('输入的数字范围不对！')
    else:
        print('输入选择有误！')


# 评论模块
@auth    
def comment():
    username = status_dict['username']
    print(f'欢迎{username}进入评论页面！')
    # 敏感词汇列表
    l1 = ['苍老师','东京热','武藤兰','波多野结衣']
    # print(os.listdir(r'D:\VScode\Python\Test_Code\day14\article'))
    files_list = os.listdir(r'D:\VScode\Python\Test_Code\day14\article')
    for index,file in enumerate(files_list):
        print(index,file)
    choose_num = input('选择需要评论的文章：')
    if choose_num.isdecimal():
        choose_num = int(choose_num)
        choose_file = files_list[choose_num]
        with open(f'day14\\article\\{choose_file}',encoding='utf-8',mode='r') as f1:
            print(f1.read())
        comments = input('请输入评论：')
        for word in l1:
            if word in comments:
                comments = comments.replace(word,'*' * len(word))
        with open(f'day14\\article\\{choose_file}',encoding='utf-8',mode='a') as f2:
            f2.write('\n来自(用户名)'+username+'的评论:\n')
            f2.write(f'{comments}'+'\n')
            print('发表评论成功！')
    else:
        print('选择评论的文章错误！')

# 日志模块
@auth    
def dariy():
    username = status_dict['username']
    print(f'欢迎{username}进入日记页面！')

# 收藏模块
@auth  
def collection():
    username = status_dict['username']
    print(f'欢迎{username}进入收藏页面！')

# 注销功能
def logout():
    status_dict['username'] = None
    status_dict['password'] = None
    status_dict['status'] = None
    print('注销账号成功!')
    print(status_dict)

# 主函数
def main():
    while True:
        choose_list = ['请登录','请注册','进入文章页面','进入评论页面','进入日志页面','进入收藏页面','注销账号','退出整个程序']
        for index,value in enumerate(choose_list):
            print(f'{index+1}. {value}')
        choose_num = input('请输入要选择的【序号】:')
        if choose_num.isdecimal():
            choose_num = int(choose_num)
            if 0 < choose_num <= len(choose_list):
                if choose_num == 1:
                    login()
                elif choose_num == 2:
                    register()
                elif choose_num == 3:
                    article()
                elif choose_num == 4:
                    comment()
                elif choose_num == 5:
                    dariy()
                elif choose_num == 6:
                    collection()
                elif choose_num == 7:
                    logout()
                else:
                    print('Bye！再见！')
                    break 
            else:
                print('输入的数字序号已超出范围值，请检查后再重新输入！')
        else:
            print('输入数据格式有误，请检查后再重新输入！')


if __name__ == '__main__':
    main()
