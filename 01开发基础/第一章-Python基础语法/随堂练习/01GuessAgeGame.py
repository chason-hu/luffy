#!/usr/bin/env python
# -*- coding:utf-8 -*-

age = 30
chance = 3

while True:
    guess_age = int(input("Please guess my age:"))
    chance -= 1

    if guess_age > age:
        print("Try smaller!")
    elif guess_age < age:
        print("Try bigger!")
    else:
        print("Bingo!")
        break

    if chance == 0:
        print("Exit..")
        break
    else:
        print("Remain %d chance" % chance)

