"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""
from venv import logger



while True:
    list=input("请输入三个数字，中间用空格隔开:").split(" ")
    list_new=[]
    for element in list:
        list_new.append(int(element))
        list_new.sort()
    print(list_new)
