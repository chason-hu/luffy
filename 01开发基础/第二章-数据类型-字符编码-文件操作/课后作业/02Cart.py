#!/usr/bin/env python
# -*- coding:utf-8 -*-

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]


# format print goods
def print_goods(goods):
    def ljust2(istr, width=10):
        istr = str(istr)
        str_len = len(istr.encode("GB2312"))
        if width > str_len:
            istr += " " * (width - str_len)

        return istr

    print("%s%s%s" % (ljust2("编号"), ljust2("商品"), ljust2("价格")))
    print("%s%s%s" % (ljust2("===="), ljust2("===="), ljust2("====")))
    for i in range(len(goods)):
        print("%s%s%s" % (ljust2(i), ljust2(goods[i]["name"]), ljust2(goods[i]["price"])))


# highlight print
def print_highlight(line):
    print("\033[32;0m{}\033[0m".format(line))


# initial
usrname=input("请输入用户名：")
passwd=input("请输入用密码：")

if usrname == "hcc" and passwd =="888":

    cart = list()
    salary = input("请输入您的工资：")
    while not salary.isdigit():
        salary = input("您输入的工资有误，请重新输入：")
    balance = int(salary)

    print_goods(goods)

    while True:
        user_input = input("输入[编号]购买/[exit]提出：")
        if user_input == "exit":
            goods_set = set(cart)
            print("=========")
            print("商品清单：")
            for g in goods_set:
                print("{0} * {1} = ￥{2}".format(goods[g]["name"], cart.count(g), cart.count(g) * int(goods[g]["price"])))
            print_highlight("账户余额：￥{0}".format(balance))
            break
        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input < len(goods):
                if balance >= goods[user_input]["price"]:
                    cart.append(user_input)
                    balance -= goods[user_input]["price"]
                    print_highlight("商品已加入购物车！")
                else:
                    print_highlight("购买失败，余额不足！")
            else:
                print("输入有误！")
        else:
            print("输入有误！")
else:
    print_highlight("用户名或密码错误")
