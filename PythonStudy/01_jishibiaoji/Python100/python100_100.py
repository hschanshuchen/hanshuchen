"""
列表转换为字典。
"""

# 第一种
num_list = ["001","002","003","004"]
name_list = ["韩书琛" ,"冯亚" ,"宋晓宇" ,"侯斌"]

dict_01 = dict(zip(num_list , name_list))

print(dict_01)


# 第二种
list_01 = [["001","韩书琛"],["002","冯亚"],["003","宋晓宇"]]

print(dict(list_01))
