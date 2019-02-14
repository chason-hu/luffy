#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("object.txt", "r", encoding="utf-8")

for line in f.readlines():
    # print("cleansePutExch{}".format("".join([c.capitalize() for c in line.split("_")])), end="")
    print("Pkg{}".format("".join([c.capitalize() for c in line.split("_")])), end="")
f.close()
