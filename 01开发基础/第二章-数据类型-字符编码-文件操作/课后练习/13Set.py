#!/usr/bin/env python
# -*- coding:utf-8 -*-

l1 = [11, 22, 33]
l2 = [22, 33, 44]
s1 = set(l1)
s2 = set(l2)

print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
