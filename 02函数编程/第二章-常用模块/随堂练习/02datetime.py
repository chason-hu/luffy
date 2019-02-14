#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import time

print(datetime.datetime.now())

# 时间戳转data类型
datetime.date.fromtimestamp(time.time())

# 时间戳转datetime类型
datetime.datetime.fromtimestamp(time.time())

# 时间运算

print(datetime.datetime.now() + datetime.timedelta(days=1))


print(datetime.datetime.now().replace(year=2018,month=12))