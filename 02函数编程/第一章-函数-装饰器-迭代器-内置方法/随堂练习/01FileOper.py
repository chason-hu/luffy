#!/usr/bin/env python
# -*- coding:utf-8 -*-
import chardet

f = open("file.txt", "rb")


def get_charset(file):
    context = bytes()
    for l in file:
        context += l
        cd = chardet.detect(context)
        if cd.get("confidence") >= 0.9:
            cs = cd.get("encoding")
            break
    # file.seek(0)
    return cs


charset = get_charset(f)

for line in f:
    print(line.decode(charset), end="")
