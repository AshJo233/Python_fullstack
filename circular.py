"""
计算圆形的周长和面积
"""

import math


radius = float(input("请输入半径:"))
perimeter = 2 * math.pi * radius
area = math.pi * (radius * radius)

print("周长：%.1f" % perimeter)
print("面积：%.1f" % area)