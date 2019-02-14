#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os

from conf import settings


class DBNotFoundException(Exception):
    """
    自定义异常：账户不存在
    """

    def __init__(self):
        self.msg = "账户不存在，请至银行开卡"

    def __str__(self):
        return self.msg


def gen_db_file_name(account_name, *args, **kwargs):
    """
    生成指定账户DB文件名称
    :param account_name:
    :param args:
    :param kwargs:
    :return:
    """
    return os.path.join(settings.BASE_DIR, "db", "accounts", "{}.json".format(account_name))


def get_db_file(account_name, *args, **kwargs):
    """
    获取指定账户DB文件
    :param account_name:
    :param args:
    :param kwargs:
    :return:
    """
    db_file = gen_db_file_name(account_name)
    # 若账户不存在，抛出异常
    if not os.path.exists(db_file):
        raise DBNotFoundException()
    return db_file


def load_account_db(account_name, *args, **kwargs):
    """
    加载指定账户DB
    :param account_name: 
    :param args: 
    :param kwargs: 
    :return: 
    """
    db_file = get_db_file(account_name)

    return json.load(open(db_file, "r", encoding=settings.DB_ENCODING))


def dump_account_db(account_db, *args, **kwargs):
    """
    更新指定账户DB
    :param account_name:
    :param account_db:
    :param args:
    :param kwargs:
    :return:
    """
    db_file = get_db_file(account_db["account_name"])

    json.dump(account_db, open(db_file, "w", encoding=settings.DB_ENCODING))
