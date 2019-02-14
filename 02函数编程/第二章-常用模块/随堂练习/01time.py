#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

# 时间戳
print(time.time())

# 本地时间
print(time.localtime())

# UTC时间
print(time.gmtime())

# 时间戳转时间
print(time.localtime(1547903539))

# 时间转时间戳
print(time.mktime(time.localtime()))

# sleep
time.sleep(1)

# 时间格式化成美式格式
print(time.asctime())
print(time.ctime())

# 时间格式化
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 字符串转时间
print(time.strptime("2019-01-19 21:19:29","%Y-%m-%d %H:%M:%S"))
