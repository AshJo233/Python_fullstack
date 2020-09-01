#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :json_demo.py
@Description   :
@Datatime      :2020/09/06 16:16:41
@Author        :AshJo
@Version       :v1.0
'''

import json


l1 = [1, 2, 3]
# d1 = {'name':'Tony','age':18,'working':True}
# t1 = ('apple','orange','grape')
# 将指定的对象转换成json格式的字符串
s = json.dumps(l1)
print(s, type(s))


# 将json内容写入到文件
# with open(r'day16\b.txt',encoding='utf-8',mode='at') as f:
#     json.dump(s,f)


# 从文件中反序列化
# with open(r'day16\b.txt',encoding='utf-8') as f:
#     res = json.load(f)
#     print(res)

# json.dumps(obj)
# json.dump(obj,f)
# json.loads(s)
# json.load(f)