#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
题目：输出指定格式的日期。
"""
import datetime

# 输出今日日期
print(datetime.date.today().strftime("%d-%m-%Y"))


# 创建日期对象
date=datetime.date(1978,3,6)
print(date.strftime("%Y-%m-%d"))

# 日期运算
datenew=date+datetime.timedelta(1)
print(datenew)

# 日期替换
datenew01=datenew.replace(1999,9,9)
print(datenew01)