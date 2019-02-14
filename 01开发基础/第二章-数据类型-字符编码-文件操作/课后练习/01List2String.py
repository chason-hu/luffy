#!/usr/bin/env python
# -*- coding:utf-8 -*-

li = ['alex', 'eric', 'rain']
s = ""
n = 1
for i in li:

    if n == 1:
        s = str(i)
    else:
        s += "_" + str(i)

    n += 1

print(s)

print("_".join([str(i) for i in li]))
