#!/usr/bin/env python
# -*- coding:utf-8 -*-

# a
print("[a------]")
n = 2
result = 0
express = "0"
while n <= 100:

    if n % 2 == 0:
        result += n
        express = express + "+" + str(n)
    else:
        result -= n
        express = express + "-" + str(n)
    n += 1

print("%s = %d" % (express, result))

# b
print("[b------]")
n = 0
while n < 12:
    n += 1
    if n in (6, 10):
        continue
    else:
        print(n)

# c
print("[c------]")
n = 0
switch_flag = False
while n <= 50:
    if switch_flag:
        print(n)
    else:
        print(100 - n)
        if n == 50:
            n = 0
            switch_flag = True

    n += 1

# d
print("[d------]")
n = 1
while n <= 100:
    if n % 2 == 1:
        print(n)
    n += 1

# e
print("[e------]")
n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1
