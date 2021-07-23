"""
题目：判断101-200之间有多少个素数，并输出所有素数。
"""
list_0=[]
leap=1
for num in range(101,201):
    for i in range(2,num):
        if num % i ==0:
            leap=0
            break
    if leap==1:
        list_0.append(num)
    leap=1
print(list_0)
print(len(list_0))