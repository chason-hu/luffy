#!/usr/bin/env python
# -*- coding:utf-8 -*-
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


menu_list = [menu]
print("输入相应的[地点]进入下一级菜单,[back]返回上一级菜单,[exit]退出菜单")
while True:

    cur_menu = menu_list[-1]
    if len(menu_list) > 1:
        pri_menu = menu_list[-2]
    else:
        pri_menu = menu_list[-1]

    print("=====\n" + "\n".join(cur_menu.keys()) + "\n=====")
    user_input = input("[输入]:")
    if user_input in cur_menu.keys():
        menu_list.append(cur_menu[user_input])
    elif user_input == "back":
        if len(menu_list) > 1:
            menu_list.remove(cur_menu)
    elif user_input == "exit":
        print("退出菜单")
        break
    else:
        print("您的输入有误，请重新输入")

