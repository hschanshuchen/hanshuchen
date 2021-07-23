"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""


flag=1
while flag:
    score=float(input("请输入成绩："))
    if score>=0 and score!="q":
        if score>=90:
            grade = "A"
        elif score>=60:
            grade = "B"
        else:
            grade = "C"
        print(grade)
    else:
        print("请输入正确的分数")
