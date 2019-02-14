#!/usr/bin/env python
# -*- coding:utf-8 -*-

chance = 3
print("==欢迎登录土豪专用小金库==")
while chance > 0:
    chance -= 1
    username = input("请输入您用户名：")
    password = input("请输入您的密码：")
    if username == "hcc" and password == "888":
        print("登录成功！")
        print("您当前的余额为：￥0.0")
        break
    else:
        if chance == 0:
            print("退出系统")
            break
        print("您输入的用户名密码不正确，请重新输入，还有%s次机会" % chance)

