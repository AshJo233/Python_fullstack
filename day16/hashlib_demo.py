#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Filename      :hashlib_demo.py
@Description   :加密
@Datatime      :2020/09/07 13:54:10
@Author        :AshJo
@Version       :v1.0
"""

import hashlib
import time
"""
md5 加密算法：

给一个数据加密的三大步骤：
1.获取一个加密对象
2.使用加密对象的update，进行加密，update方法可以调用多次
3.通常通过hexdigest获取加密结果，或digest()方法

"""
# 获取一个加密对象
# m = hashlib.md5()
# 使用加密对象的update方法，进行加密
# m.update('abc喜羊羊与灰太狼'.encode('utf-8'))

# 通过hexdigest()获取加密结果
# res = m.hexdigest()
# print(res, type(res)) # 6c00f40e37d2c13654692b2215c543aa

# 给一个数据加密
# 验证：用另一个数据加密的结果和第一次加密的结果比对
# 结果相同，说明与原文一致，不同说明与原文不一致

# 不同加密算法：实际上就是加密结果的长度不相同
# s = hashlib.sha224()
# s.update(b'abc')
# print(len(s.hexdigest()))
#
# print(len(hashlib.md5().hexdigest()))
# print(len(hashlib.sha256().hexdigest()))

# 在创建加密对象时，可以指定参数，称为salt
# m = hashlib.md5(b'abc')
# print(m.hexdigest()) # 900150983cd24fb0d6963f7d28e17f72

# m = hashlib.md5()
# m.update(b'abc')
# print(m.hexdigest()) # 900150983cd24fb0d6963f7d28e17f72


# 利用加密模块，作为数据比对，实现模拟简单的用户注册登录功能

def get_md5(username, password):
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()


def register(username, password):
    res = get_md5(username, password)
    with open('login.txt', mode='at', encoding='utf-8') as f:
        f.write(res + '\n')
    print('注册成功...等待3秒后返回')
    time.sleep(3)
    return Tru
e

def login(username, password):
    res = get_md5(username, password)
    with open('login.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            if res == line.strip():
                return True
        else:
            return False


def main():
    while True:
        try:
            op = int(input('1.注册 | 2.登录 | 3.退出：'))
            if op == 1:
                username = input('请输入用户名')
                password = input('请输入密码')
                register(username, password)
            elif op == 2:
                username = input('请输入用户名')
                password = input('请输入密码')
                res = login(username, password)
                if res:
                    print('登录成功！')
                else:
                    print('登录失败！')
            elif op == 3:
                break
            else:
                print('你的输入有误！')
        except ValueError:
            print('你的输入有误！')


if __name__ == '__main__':
    main()

