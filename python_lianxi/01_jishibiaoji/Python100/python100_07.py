"""
题目：将一个列表的数据复制到另一个列表中。
"""
while True:
    list=input("请输入列表找那个的元素，中间用，隔开：").split(",")
    list_new=list[:]
    print(list_new)