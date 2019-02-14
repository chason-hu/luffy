#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
id = re.search("(?P<province>\d{3})(?P<city>\d{3})(?P<birth>\d{4})","320283198911152279")
print(id.groupdict())
