"""
百分制成绩转换为等级制成绩
"""

score = float(input("Please input a score:"))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print("The grade is:",grade)