#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

age = random.randint(1, 100)
chance = 3

while True:
    guess_age = int(input("Please guess my age[1-100]:"))
    chance -= 1

    if guess_age > age:
        print("Try smaller!")
    elif guess_age < age:
        print("Try bigger!")
    else:
        print("Bingo!")
        break

    if chance == 0:
        print("Your chance has used up!")
        continue_game = input("Play again(y/n)?:")
        if continue_game == 'y':
            print("Give you 3 more chance!")
            chance = 3
        else:
            print("Exit...")
            break
    else:
        print("Remain %d chance" % chance)
