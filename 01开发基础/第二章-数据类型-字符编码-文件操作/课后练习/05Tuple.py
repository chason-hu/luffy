#!/usr/bin/env python
# -*- coding:utf-8 -*-

tu=('alex', 'eric', 'rain')

print(tu)
print(len(tu))

print(tu[0:2])

for i in range(len(tu)):
    print(i)

for n,i in enumerate(tu,10):

    print(n,i)
