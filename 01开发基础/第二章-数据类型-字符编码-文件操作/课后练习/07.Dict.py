#!/usr/bin/env python
# -*- coding:utf-8 -*-

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

print(dic)

for k in dic.keys():
    print(k)


for k in dic.keys():
    print(dic[k])

dic["k4"] = "k4"
print(dic)

dic["k1"] = "alex"
print(dic)

dic["k3"].append("44")
print(dic)

dic["k3"].insert(0,18)
print(dic)