#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = "alex"
print(s)
print(list(s))
print(tuple(s))

li = ["alex", "seven"]
print(tuple(li))

tu = ('Alex', "seven")
print(list(tu))

li = ["alex", "seven"]

dic = {}
for k,i in enumerate(li,10):
    dic[k] = i

print(dic)