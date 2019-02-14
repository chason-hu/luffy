#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

auth_file = "Login.json"

auth = dict()
auth = json.load(open(auth_file, "r"))
chance = 3
print("==欢迎登录土豪专用小金库==")
while chance > 0:
    chance -= 1
    username = input("请输入您用户名：")
    password = input("请输入您的密码：")
    if username in auth.keys():
        if auth[username]["is_lock"] == "Y":
            print("账户被锁定，请联系管理员解锁！")
            break
        else:
            if password == auth[username]["pwd"]:
                print("登录成功！")
                print("您当前的余额为：￥%d" % auth[username]["balance"])
                break

            else:
                if chance == 0:
                    auth[username]["is_lock"] = "Y"
                    json.dump(auth, open(auth_file, "w"))
                    print("账户被锁定，请联系管理员解锁，退出系统！")
                    break
            print("您输入的用户名密码不正确，请重新输入，还有%s次机会" % chance)
