#!/usr/bin/env python
# -*- coding:utf-8 -*-

li = ["al ec", " ari c", "A lex", "Tony", "ra in"]

print(li)
for i in range(len(li)):
    li[i] = li[i].replace(" ", "")
print(li)

for i in li:
    if i.startswith("a") or i.startswith("A") or i.endswith("c"):
        print(i)

tu = ("a lec", " a ric", "Ale x", "Ton y", "rain")



dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

