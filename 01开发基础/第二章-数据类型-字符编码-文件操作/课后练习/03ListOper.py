#!/usr/bin/env python
# -*- coding:utf-8 -*-


li = ['alex', 'eric', 'rain']
print(li)

li.append("seven")
print(li)

li.insert(0, "Tony")
print(li)

li[1] = "Kelly"
print(li)

li.remove("eric")
print(li)

print(li[2])
del li[2]
print(li)

print(li[1:4])
del li[1:4]
print(li)

li = ['alex', 'eric', 'rain']
li.reverse()
print(li)

for i in range(len(li)):
    print(i)

for n,i in enumerate(li):
    print(n,i)