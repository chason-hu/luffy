#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# 获取当前工作目录
print(os.getcwd())

# 返回指定目录下所有文件和目录
print(os.listdir())

# 删除文件
# os.remove()

# 删除多个目录
# os.removedirs()

# 判断是否文件
print(os.path.isfile("04os.py"))

# 判断是否目录
print(os.path.isdir("../"))

# 判断是否是绝对路径
print(os.path.isabs("../"))

# 判断路径是否真实存在
print(os.path.exists("04os.py"))

# 返回路径的目录和文件名
print(os.path.split("../04os.py"))

# 分离扩展名
print(os.path.splitext("04os.py"))

# 获取路径名
print(os.path.dirname("../04os.py"))

# 获取绝对路径
print(os.path.abspath("04os.py"))
