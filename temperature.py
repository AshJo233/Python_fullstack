"""
摄氏度℃ 转化 为 华氏度℉
"""


# centigrade = float(input("Please intput a centigrade:"))
# Fahrenheit_degree = centigrade * 1.8 + 32
# print('%f ℃  =  %f ℉' % (centigrade,Fahrenheit_degree))


"""
摄氏度和华氏度的相互转换
"""

def Centigrade():
    c = float(input("Please intput a centigrade:"))
    f = (c * 1.8) + 32
    print('%f ℃  =  %f ℉' % (c,f))

def Fahrenheit():
    f = float(input("Please intput a fahrenheit:"))
    c = (f - 32) / 1.8
    print('%f ℉ =  %f ℃' % (f,c))


def main():
    choose = input("Choose 1(Centigrade) or 2(Fahrenheit):")
    if choose == '1':
        Centigrade()
    elif choose == '2':
        Fahrenheit()
    else:
        print("Your input is Error!")
        exit()


if __name__ == "__main__":
    main()