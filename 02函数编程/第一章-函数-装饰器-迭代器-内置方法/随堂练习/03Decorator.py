#!/usr/bin/env python
# -*- coding:utf-8 -*-

is_login = False


def login(auth_type):
    def auth(func):

        def inner(*args, **kwargs):

            global is_login
            if is_login:
                print("已认证")
            else:
                _user = input("请输入{}用户：".format(auth_type))
                _passwd = input("请输入密码：")

                if _user == "hcc" and _passwd == "888":
                    is_login = True

            if is_login:
                func(*args, **kwargs)

        return inner

    return auth


@login("qq")
def home():
    print("home")


@login("weixin")
def studdy_center(course):
    print(course)


@login("phone")
def free_video():
    print("Mysql从删库到跑路")


home()
studdy_center("python全栈中级")
free_video()
