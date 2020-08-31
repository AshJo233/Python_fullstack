"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

# import random

# answer = random.randint(1,100)
# counter = 0
# min = 1
# max = 100

# while True:
#     counter += 1
#     guess = int(input("Pleaes Enter a numer (%d~%d):" % (min,max)))
#     if guess < answer and min < guess and guess < max:
#         print("大一点")
#         min = guess
#     elif guess > answer and min < guess and guess < max:
#         print("小一点")
#         max = guess
#     elif guess == answer:
#         print("恭喜你，猜对了")
#         break
#     else:
#         print("输入格式错误！")
#         exit()

# if counter < 5:
#     print("你真是个小天才")
# else:
#     print("智商不够，多喝六个核桃")
    


# flag = True
# while flag:
#     print(1)
#     print(2)
#     print(3)
#     flag = False
#     print(4)

"""
1到100的总和
"""
# sum = 0
# count = 1
# while count <= 100:
#     sum += count
#     count += 1
# print(sum)

"""
输出1-100的所有偶数或者奇数
"""

# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1

# count = 1
# while count <= 100:
#     if count % 2 != 0:
#         print(count)
#     count += 1


# flag = True
# while flag:
#     print(1)
#     print(22)
#     flag = False
#     continue
#     print(333)
#     print(4444)
'''
输出1 2 3 4 5 6 8 9 10
'''

# count = 1
# while count <= 10:
#     if count == 7:
#         count += 1
#     print(count)
#     count += 1

# count = 1
# while count <= 10:
#     if count == 7:
#         pass
#     else:
#         print(count)
#     count += 1

# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)

'''
输出1-2+3-4+5.....-100的和
'''
count = 1
sum = 0
while count < 100:
    if count % 2 == 0:
        sum -= count
    else:
        sum += count
    count += 1
print(sum)

    
