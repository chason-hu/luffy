#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json
import os

from core import db_handler
from conf import settings

sample = {
    "password": "123456",
    "balance": 0,
    "credit": 15000,
    "status": 0
}


def create_account(account_name, *args, **kwargs):
    db_file = db_handler.gen_db_file_name(account_name)
    if not os.path.exists(db_file):
        account_db = sample
        account_db["account_name"] = account_name
        json.dump(account_db, open(db_file, "w", encoding=settings.DB_ENCODING))
