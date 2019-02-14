#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import time


# Format Print Goods
def print_goods(goods):
    def ljust2(istr, width=10):
        istr = str(istr)
        str_len = len(istr.encode("GB2312"))
        if width > str_len:
            istr += " " * (width - str_len)

        return istr

    print("{0}{1}{2}".format(ljust2("编号"), ljust2("商品"), ljust2("价格")))
    print("{0}{1}{2}".format(ljust2("===="), ljust2("===="), ljust2("====")))
    for i in range(len(goods)):
        print("{0}{1}{2}".format(ljust2(i), ljust2(goods[i]["name"]), ljust2(goods[i]["price"])))


# Highlight Print String
def print_highlight(line):
    print("\033[32;0m{}\033[0m".format(line))


# Print Order/Cart
def print_order(goods, order, type="order"):
    goods_set = set(order)
    if type == "order":
        print("订单清单：")
    else:
        print("购物车清单：")
    for g in goods_set:
        print(
            "{0} * {1} = ￥{2}".format(goods[g]["name"], order.count(g),
                                      order.count(g) * int(goods[g]["price"])))
    print("总计: ￥{0}".format(sum([goods[g]["price"] for g in order])))
    print("=========")


# Initial DB Information From File
db = json.load(open("Cart.json", "r", encoding="utf-8"))
t_goods = db["goods"]
t_auth = db["auth"]
t_order = db["order"]
t_balance = db["balance"]
t_cart = db["cart"]

# Authentication
print("=========欢迎登录路飞学城小卖部========")
usr = input("请输入用户名：").strip()
pwd = input("请输入用密码：")

if t_auth.get(usr) == pwd:

    # Get User's Information

    # Current Cart
    cart = t_cart.get(usr)

    if cart:
        # Total Price Of Current Cart
        cart_tt_price = sum([t_goods[g]["price"] for g in cart])
    else:
        cart = list()
        db["cart"][usr] = cart
        cart_tt_price = 0

    # Balance
    balance = t_balance.get(usr)

    if not balance:
        balance = 0
        db["balance"][usr] = balance

    # History Orders
    order = t_order.get(usr)
    if not order:
        order = dict()
        db["order"][usr] = order

    print_highlight("登录成功，账户余额：￥{0}".format(balance))

    # Show All Goods
    print_goods(t_goods)

    while True:
        # Print Operation Hint
        user_input = input("输入 1.[编号]加入购物车 2.[list]查看购物车和余额 3.[pay]下单 4.[his]查看历史订单 4.[charge]充值 2.[exit]退出 :")

        # Exit
        if user_input == "exit":
            print_highlight("账户余额：￥{0}".format(balance))
            print("退出系统")
            break

        # List
        if user_input == "list":
            print_order(t_goods, cart, "cart")
            print_highlight("账户余额：￥{0}".format(balance))

        # Pay
        elif user_input == "pay":
            if len(cart) > 0:
                # Balance Change
                balance -= cart_tt_price

                # Generate Order Key (Time)
                order_time = time.strftime("%Y-%m-%d %H:%M:%S")
                order[order_time] = cart.copy()

                # Print Cart
                print_highlight("支付成功")
                print_order(t_goods, cart, "order")

                # Print Balance
                print_highlight("账户余额：￥{0}".format(balance))

                # Clean Cart
                cart.clear()
            else:
                print_highlight("购物车中没有商品")

        # His
        elif user_input == "his":

            # Loop Print Order
            if order:
                for o in order.keys():
                    print("订单时间:{0}".format(o))
                    print_order(t_goods, order[o], "order")
            else:
                print("无购买历史")

        # Charge
        elif user_input == "charge":
            # Input Charge Amount
            amount = input("请输入需要充值的金额：")

            # Validate
            while not amount.isdigit():
                amount = input("您输入的金额不正确，请重新输入：")

            # Balance Charged
            amount = int(amount)
            balance += amount

        # Pick Good
        elif user_input.isdigit():
            user_input = int(user_input)
            # Validate Goods Index
            if user_input < len(t_goods):
                # Update Cart Only Balance Is Enough
                if balance >= cart_tt_price + t_goods[user_input]["price"]:
                    cart.append(user_input)
                    cart_tt_price += t_goods[user_input]["price"]
                    print_highlight("商品已加入购物车")
                else:
                    print_highlight("加入购物车失败，余额不足")
            else:
                print("没有该商品")
        else:
            print("输入有误")

    # Update User's Information

    t_cart[usr] = cart
    t_balance[usr] = balance
    t_order[usr] = order

else:
    print_highlight("用户名或密码错误")

# Update DB Information
db["order"] = t_order
db["balance"] = t_balance
db["cart"] = t_cart

# Dump Information Into File
json.dump(db, open("Cart.json", "w", encoding="utf-8"))
