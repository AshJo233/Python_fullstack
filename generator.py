#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename      :generator.py
@Description   :
@Datatime      :2020/08/29 11:11:55
@Author        :AshJo
@Version       :v1.0
'''

# 生成器函数
def func():
    print(111)
    print(222)
    #return 3
    yield 3

# ret = func()
# print(ret)
#print(next(ret))

# 吃包子

def cbz():
    l1 = []
    for i in range(1,101):
        l1.append(f'{i}号包子')
    return l1
# ret = cbz()
# print(ret)

def gen_cbz():
    for i in range(1,101):
        yield f'{i}号包子'
# ret = gen_cbz()
# for i in range(20):
#     print(next(ret))



# yield from的使用
l1 = ['喜羊羊','灰太狼','懒羊羊']
l2 = ['孙悟空','猪八戒','二郎神']

def yi_fr():
    yield from l1
    yield from l2

g = yi_fr()
while True:
    try:
        for i in range(9):
            print(next(g))
    except StopIteration:
        break


# yield 与 return 嵌套使用
class TestYield:
    def gen_iterator(self):
        for j in range(3):
            print(f"do_something-{j}")
            # yield在for循环内部
            yield j

    def gen_iterator_middle(self):
        print(f"gen_iterator_middle")
        # 返回的是迭代器的句柄，所以加一层return不影响是可以理解的
        return self.gen_iterator()

    def call_gen_iterator(self):
        # yield并不是直接返回[0,1,2]，执行下边这句后result_list什么值都没有
        result_list = self.gen_iterator_middle()
        # i每请求一个数据，才会触发gen_iterator生成一个数据
        for i in result_list:
            print(f"call_gen_iterator-{i}")

if __name__ == "__main__":
    obj = TestYield()
    obj.call_gen_iterator()



# 列表推导式

# 循环模式
l1 = [i for i in range(1,101)]
print(l1)

# 筛选模式
l2 = [i for i in range(1,101) if i % 2 == 0]
print(l2)


lst = [i**2 for i in range(1,11)]
print(lst)


# 生成器表达式

l3 = (i for i in range(11))
print(l3)
for i in l3:
    print(i)