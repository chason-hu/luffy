#!/usr/bin/env python
# -*- coding:utf-8 -*-

tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

print(tu)
tu[1][2]["k2"].append("Seven")

print(tu)