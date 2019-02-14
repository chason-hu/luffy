#!/usr/bin/env python
# -*- coding:utf-8 -*-


li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

dic = {"k1": [], "k2": []}

for i in li:
    if i < 66:
        dic["k1"].append(i)
    elif i > 66:
        dic["k2"].append(i)
    else:
        continue

print(dic)
