'''
输入一个正整数判断它是不是素数
提示：素数指的是只能被1和自身整除的大于1的整数。
'''

from math import sqrt

# num = int(input("Please input a number:"))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2,end+1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num > 1:
#     print("%d is a Prime number" % num)
# else:
#     print("%d is not a Prime number" % num)

'''
输出100以内的所有素数
'''
num = 0
while num <= 100:
    is_prime = True
    end = int(sqrt(num))
    for x in range(2,end+1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        print("%d is a Prime number" % num)
    # else:
    #     print("%d is not a Prime number" % num)
    num += 1


