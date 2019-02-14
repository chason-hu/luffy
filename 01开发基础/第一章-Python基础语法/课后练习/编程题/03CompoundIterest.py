#!/usr/bin/env python
# -*- coding:utf-8 -*-

principal = 10000
rate = 0.0325
target = 20000
n = 0
while principal < target:
    principal *= (1 + rate)
    n += 1
print(n)
