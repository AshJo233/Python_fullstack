"""
输入三条边长,如果能构成三角形就计算周长和面积
"""

a = float(input("1.Please input a value for a:"))
b = float(input("2.Please input a value for b:"))
c = float(input("3.Please input a value for c:"))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    p = perimeter / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("三角形周长：",perimeter)
    print("三角形面积：",area)
else:
    print("不能构成三角形!")