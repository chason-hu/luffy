#!/usr/bin/env python
# -*- coding:utf-8 -*-

names = ["old_driver", "rain", "jack", "shanshan", "peiqi", "black_girl"]
li = [1, 2, 3, 4, 54, 2, 4]
names.extend(li)
print(names)

print(names[-3:])

print(li.index(2, li.index(2) + 1))

