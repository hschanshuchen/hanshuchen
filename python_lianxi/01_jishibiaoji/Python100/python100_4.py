"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""
while True:
    dataList=[]
    dataList=input("请输入年月日，中间以.隔开，如：2021.3.23：").split(".")
    newList = []
    for j in dataList:
        newList.append(int(j))
    y=newList[0]
    m=newList[1]
    d=newList[2]
    sum = 0
    if y%400==0 or y%4==0 or y%100==0:
        monthList=[31,29,31,30,31,30,31,31,30,31,30,31]
        if 1<m<=12:
            for i in range(0,m-1):
                sum= sum + monthList[i]
            sum = sum +d
            print("今天是第",sum,"天")
        elif m==1:
            sum = d
            print("今天是第",sum,"天")
        else:
            print("输入错误")
    else:
        monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if 1<m<=12:
            for i in range(0,m-1):
                sum = sum + monthList[i]
            sum = sum+d
            print("今天是第",sum,"天")
        elif m==1:
            sum = d
            print("今天是第",sum,"天")
        else:
            print("输入错误")