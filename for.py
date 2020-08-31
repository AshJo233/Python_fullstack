# """
# 整数数列，for循环 1 - 100 求和
# """
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

# """
# 使用步长的方式，for循环 1 - 100 的偶数求和
# """
# sum = 0
# for x in range(2,101,2):
#     sum += x
# print(sum)


# """
# for循环 1 - 100 的偶数求和，使用if判断偶数
# """
# sum = 0
# for a in range(1,101):
#     if a % 2 == 0:  
#         sum += a
# print(sum)

# len内置函数： 获取可迭代对象的元素总个数
# s1 = "VisualStudioCode"
# index = 0
# while index < len(s1):
#     print (s1[index])
#     index += 1
# for i in s1:
#     print(i)

l1 = []
for i in range(100,9,-1):
    if i % 2 == 0:
        l1.append(i)    
    else:
        pass
print(l1)

l2 = []
for y in l1:
    if y % 4 == 0:
        l2.append(y)
    else:
        pass
print(l2)