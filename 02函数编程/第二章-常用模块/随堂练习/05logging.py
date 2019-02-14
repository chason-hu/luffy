#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

class ignoreDBLog(logging.Filter):

    def filter(self, record):

        return "DB" not in record.getMessage()


# 1.生成logger对象
logger = logging.getLogger("web")
logger.setLevel(logging.INFO)

# 2.生成handler对象
ch = logging.StreamHandler()
fh = logging.FileHandler("web.log")

# 2.1把handler对象绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

# 3.生成formatter对象
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
console_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

# 3.1把formatter对象板顶到handler对象
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.addFilter(ignoreDBLog())
logger.debug("debug log")
logger.info("info log")
logger.error("DB log")

