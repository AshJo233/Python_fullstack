
# 利用切片和步长，完全倒序输出一个字符串
# s = "VisualStudioCode"
# s2 = s[::-1]
# print(s2)

# 字符串转换大小写
# s3 = s.upper()
# s4 = s.lower()
# print(s3)
# print(s4,type(s4))

#应用： 实现登录时的验证码不区分大小写
# count = 0
# while count < 3:
#     username = input("用户名：")
#     password = input("密码：")
#     code = 'QweR'
#     your_code = input("验证码：")
#     if your_code.lower() == code.lower():
#         if username == 'AshJo' and password == '123456':
#             print("登录成功！")
#             exit()
#         else:
#             print("登录失败！请检查用户名和密码")
#             count += 1
#     else:
#         print("验证码有误！")
#         count += 1
# else:
#     print("登录尝试次数过多，稍后再试")
#     exit()


# split 字符串元素分割成列表的数据类型
# s1 = "红红火火,恍恍惚惚,换哼"
# l1 = ['灰太狼','懒洋洋','喜羊羊']

# print(s1.split())

# # join 添加分隔符
# l2 = ':'.join(l1)
# print(l2,type(l2))


# format 格式化输出

# msg = "我是{0},{1}岁,性别{2}".format('喜之郎',8,'男')
# print(msg)

# relace 字符替换
# s = '   abcdeeeffffsdfdsf: sdfsdf: asdfsd dfds   '
# print(s.replace('e','y'))

# strip 字符串删除左右边的空格
# print(s.strip())


# s = '321'

# for i in s:
#     print("倒计时{}秒".format(i))
# else:
#     print("出发！")

# print(i)



# s1 = 'baiDu.cOmsystemipaddr'
# # 首字母大写
# print(s1.capitalize())

# # 大小写转换
# print(s1.swapcase())

# # 每个单词首字母大写
# print(s1.title())

# # 居中

# print(s1.center(5,'*'))

# # 通过元素索引 find index
# print(s1.find('a'))
# print(s1.index('r'))

# 编码的转换
# 内存显示的是unicode编码，但传输和存储时需要使用非Unicode编码

# s1 = '我是你爹'
# b1 = s1.encode('utf-8')
# print(b1) # b'\xe6\x88\x91\xe6\x98\xaf\xe4\xbd\xa0\xe7\x88\xb9'

# b2 = b'\xe6\x88\x91\xe6\x98\xaf\xe4\xbd\xa0\xe7\x88\xb9'
# s2 = b2.decode('utf-8')
# print(s2)

