#!/usr/bin/env python
# -*- coding:utf-8 -*-


# def func1():
#     print("alex")
#
#     def func2():
#         print("eric")
#
#     func2()


age = 18


def func1():
    age = 72

    def func2():
        print(age)

    return func2
    # age = 73


func = func1()
func()
