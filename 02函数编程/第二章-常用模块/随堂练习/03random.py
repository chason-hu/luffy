#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import string

# 闭区间
print(random.randint(1, 100))

# 左闭右开区间
print(random.randrange(1, 100))

# 随机返回指定字符串中的字符
print(random.choice("abcdefg"))

# 随机返回指定字符串中的多个字符
print(random.sample("abcdefg", 3))

# 获取数字，ascii码字母，

string.digits
string.ascii_letters
string.hexdigits
string.ascii_lowercase

# 生成随机验证码

print("".join(random.sample(string.ascii_letters, 5)))

# 随机洗牌
a = list(range(10))
random.shuffle(a)
print(a)
