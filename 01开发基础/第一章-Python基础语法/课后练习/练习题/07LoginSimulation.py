#!/usr/bin/env python
# -*- coding:utf-8 -*-


# i.

username = input("请输入用户名：")
password = input("请输入密码：")

if username == "seven" and password == "123":
    print("登录成功！")
else:
    print("登录失败！")

# ii.

chance = 3

while chance > 0:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "seven" and password == "123":
        print("登录成功！")
        break
    else:
        print("登录失败！")
        chance -= 1

# ii.

chance = 3

while chance > 0:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if (username == "seven" or username == "alex") and password == "123":
        print("登录成功！")
        break
    else:
        print("登录失败！")
        chance -= 1
