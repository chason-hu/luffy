#!/usr/bin/env python
# -*- coding:utf-8 -*-


f = open("object.txt", "r", encoding="utf-8")

se = set([x.strip().split(":")[1].strip().strip("\"") for x in f.readlines()])
li = list(se)
li.sort()


for i in li:
    print(i)
