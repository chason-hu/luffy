#!/usr/bin/env python
# -*- coding:utf-8 -*-

from core import auth

def login():
    try:
        password_fail_times = settings.PASSWORD_FAIL_TIMES

        while not account_info.get("is_auth"):
            # 密码错误3次，锁定账户
            if password_fail_times == 0:
                account_info["account_db"]["status"] = 1
                db_handler.dump_account_db(account_info["account_db"])
                print("密码失败次数超过3次，账户已锁定,请联系管理员！")
                break

            # 输入用户名密码
            account_name = input("请输入账户名：")
            password = input("请输入密码：")

            # 获取账户信息
            return_data = db_handler.load_account_db(account_name)

            # 密码匹配则认证成功
            account_info["account_db"] = return_data
            if account_info["account_db"]["password"] == str(password):
                if account_info["status"] == 1:
                    print("账户已锁定,请联系管理员！")
                    break
                account_info["is_auth"] = True
                break
            else:
                # 密码错误重新输入
                print("密码错误，请重新输入！")
                password_fail_times -= 1
    except Exception as e:
        print(e)

def run():
    """
    运行用户程序
    :return: 
    """
    account_info = {
        "is_auth": False,
        "account_db": None
    }

    auth.auth(account_info)



def controller():
    pass
