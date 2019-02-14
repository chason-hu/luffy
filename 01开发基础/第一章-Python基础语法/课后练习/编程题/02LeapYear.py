#!/usr/bin/env python
# -*- coding:utf-8 -*-

year = int(input("请输入年份："))
if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
    print("%s是个闰年" % year)
else:
    print("%s是个平年" % year)
