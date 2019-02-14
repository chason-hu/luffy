#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import re

# global variables
tables = dict()
metadata = json.load(open("metadata.json", "r", encoding="utf-8"))


def load_table(tab_name):
    """
    load specified table's data to global tables
    :param tab_name: table name
    :param charset: character set
    :return: None
    """
    global tables
    global metadata

    tables[tab_name] = []
    for line in open(metadata.get(tab_name).get("dbfile"), "r", encoding="utf-8").readlines():
        tables[tab_name].append(line.strip().split(","))


def flush_table(tab_name):
    """
    flush specified table's data into file
    :param tab_name:table name
    :param charset:character set
    :return:
    """
    global tables
    global metadata

    f = open(metadata.get(tab_name).get("dbfile"), "w", encoding="utf-8")
    f.truncate()
    for line in tables.get(tab_name):
        f.write("{}\n".format(",".join(line)))
    f.close()


def sql_parser(sql):
    """
    Parse sql and route to executor
    :param sql:sql string
    :return: None
    """

    # udf exception
    def raise_syntax_exception():
        """
        raise syntzx exception
        :return:
        """
        raise Exception("ERROR: Syntax Error")

    # add parser
    def add_parser(sql):
        """
        add parser
        :param sql: sql string
        :return: parsed sql
        """
        expr1 = "add[\s]+(\S*)[\s]+(.*)"
        parser = re.findall(expr1, sql, re.I)

        if parser:
            parsed_sql = parser[0]
            table = table_parser(parsed_sql[0])
            row = parsed_sql[1].split(",")
            return ({"table": table, "row": row})
        else:
            raise_syntax_exception()

    # delete parser
    def del_parser(sql):
        """
        delte parser
        :param sql: sql string
        :return: parsed sql
        """
        expr1 = "del[\s]+from[\s]+(\S*)[\s]+where[\s]+(.*)"
        expr2 = "del[\s]+from[\s]+(\S*)"
        parser = re.findall(expr1, sql, re.I) or re.findall(expr2, sql, re.I)

        if parser:
            parsed_sql = parser[0]
            table = table_parser(parsed_sql if isinstance(parsed_sql, str) else parsed_sql[0])
            filters = list()
            if len(parsed_sql) == 2:
                filters = filter_parser(table, parsed_sql[1])
            return ({"table": table, "filters": filters})

        else:
            raise_syntax_exception()

    # update parser
    def upd_parser(sql):
        """
        update parser
        :param sql:
        :return:
        """
        expr1 = "update[\s]+(.*)[\s]+set[\s]+(.*)[\s]+where[\s]+(.*)"
        expr2 = "update[\s]+(.*)[\s]+set[\s]+(.*)"
        parser = re.findall(expr1, sql, re.I) or re.findall(expr2, sql, re.I)
        if parser:
            parsed_sql = parser[0]
            table = table_parser(parsed_sql[0])
            chgset = chset_parser(table, parsed_sql[1])
            filters = list()
            if len(parsed_sql) == 3:
                filters = filter_parser(table, parsed_sql[2])
            return ({"table": table, "chgset": chgset, "filters": filters})
        else:
            raise_syntax_exception()

    # find parser
    def find_parser(sql):
        expr1 = "find[\s]+(.*)[\s]+from[\s]+(.*)[\s]+where[\s]+(.*)"
        expr2 = "find[\s]+(.*)[\s]+from[\s]+(.*)"
        parser = re.findall(expr1, sql, re.I) or re.findall(expr2, sql, re.I)

        if parser:
            parsed_sql = parser[0]
            table = table_parser(parsed_sql[1])
            columns = columns_parser(table, parsed_sql[0])
            filters = list()
            if len(parsed_sql) == 3:
                filters = filter_parser(table, parsed_sql[2])

            return ({"table": table, "columns": columns, "filters": filters})
        else:
            raise_syntax_exception()

    # oper router
    if sql.lower() == "exit":
        exit(0)
    else:
        try:
            if sql.lower().startswith("add"):
                add_executor(**add_parser(sql))
            elif sql.startswith("del"):
                del_executor(**del_parser(sql))
            elif sql.lower().startswith("update"):
                upd_executor(**upd_parser(sql))
            elif sql.lower().startswith("find"):
                find_executor(**find_parser(sql))
        except Exception as e:
            print(e)


# parsers
def table_parser(table):
    """
    verify if table is exits
    :param table: table name
    :return: return striped table name
    """
    global tables
    global metadata
    tab_name = table.strip()
    if tab_name in metadata.keys():
        return tab_name
    # raise exception if table not found
    else:
        raise Exception("ERROR: Table {} Not Exits".format(tab_name))


def columns_parser(table, columns):
    """
    verify columns if exits
    :param table: table which columns belong to
    :param columns: columns
    :return: return columns list
    """
    global tables
    global metadata
    meta_cols = metadata.get(table).get("cols")
    columns = columns.strip()
    # parse * as all column
    if columns == "*":
        columns = meta_cols
    else:
        columns = [c.strip() for c in columns.split(",")]
        diff_cols = set(columns).difference(set(meta_cols))
        # raise exception if can't find column
        if diff_cols:
            raise Exception("ERROR: Column {} Not Found".format(",".join(diff_cols)))
    return columns


def chset_parser(table, chset):
    """
    verify if change set match the colums
    :param table: table name
    :param chset: change set
    :return:
    """
    global tables
    global metadata

    meta_cols = metadata.get(table).get("cols")

    chset = chset.strip().split(",")
    return_chset = list()
    for f in chset:
        f_list = [i.strip() for i in re.split("(=)", f, re.I)]
        if len(f_list) == 3:
            if f_list[0] in meta_cols:
                f_list[2] = f_list[2].strip("\'").strip("\"")
                return_chset.append(f_list)
            else:
                raise Exception("ERROR: Column {} Not Found In Set".format(f_list[0]))
        else:
            raise Exception("ERROR: Set {} Syntax Error".format(f))

    return return_chset


def filter_parser(table, filters):
    """
    verify if filters match the columns
    :param table: table name
    :param filters: filter string
    :return: return filter list
    """
    global tables
    global metadata

    meta_cols = metadata.get(table).get("cols")

    filters = filters.strip().split("and")
    spt_oper = ("=", ">", "<", "like")
    return_filters = list()
    for f in filters:
        f_list = [i.strip() for i in re.split("({})".format("|".join(spt_oper)), f, re.I)]
        if len(f_list) == 3:
            if f_list[0] in meta_cols:
                f_list[2] = f_list[2].strip("\'").strip("\"")
                return_filters.append(f_list)
            else:
                raise Exception("ERROR: Column {} Not Found In Filter".format(f_list[0]))
        else:
            raise Exception("ERROR: Filter {} Syntax Error".format(f))

    return return_filters


# verify if row can be filter
def can_be_filter(row, meta, filters):
    """
    return true if row can't be filter
    :param row:  data of a row
    :param meta: meta data of a row
    :param filters: list of the filters
    :return: True or False
    """
    result = True

    for f in filters:
        col = f[0]
        oper = f[1]
        value = f[2]  # .strip("\"").strip("\'")
        if oper == "=":
            result = result and row[meta.index(col)] == value
        elif oper == "<":
            result = result and row[meta.index(col)] < value
        elif oper == ">":
            result = result and row[meta.index(col)] > value
        elif oper == "like":
            result = result and (value in row[meta.index(col)])
        else:
            raise Exception("ERROR: Unsupported Operator {}".format(oper))
        if not result:
            return result
    return result


# CURD Executor

def add_executor(*args, **kwargs):
    """
    add data into specified table
    :param args:
    :param kwargs:
    :return: None
    """
    global tables
    global metadata

    table = kwargs.get("table")
    row = [c.strip() for c in kwargs.get("row")]

    data = tables.get(table)
    meta_cols = metadata.get(table).get("cols")
    seq = metadata.get(table).get("seq")
    uniq = metadata.get(table).get("uniq")

    need_col_n = len(set(meta_cols).difference(set(seq)))
    inst_col_n = len(row)

    def get_nextval(data, index):
        """
        get max value from a two-dim arrary' specified col index
        :param data: two-dim array
        :param index: col index
        :return:
        """
        curval = max([int(x[index]) for x in data])
        return str(curval + 1) if curval else 0

    def verify_duplicate(data, index, val):
        """
        verify is value duplicate in two-dim array's specified col
        :param data: two-dim
        :param index: col index
        :param val: value to be verified
        :return:
        """
        col_list = [x[index] for x in data]
        return val in col_list

    # no enough values
    if need_col_n > inst_col_n:
        raise Exception("ERROR: no enough values ")
    # too many values
    elif need_col_n < inst_col_n:
        raise Exception("ERROR: too many values ")
    else:
        # generate sequence based on seq metadata
        for s in seq:
            ind = meta_cols.index(s)
            row.insert(ind, get_nextval(data, ind))

        # verify uniqueness
        for u in uniq:
            ind = meta_cols.index(u)
            if verify_duplicate(data, ind, row[ind]):
                raise Exception("ERROR: found duplicate value {} in {}.{}".format(row[ind], table, u))

        # add row
        data.append(row)
        tables[table] = data
        flush_table(table)

        print("add 1 rows")


def del_executor(*args, **kwargs):
    """
    delete executor
    :param args:
    :param kwargs:
    :return: None
    """

    table = kwargs.get("table")
    filters = kwargs.get("filters")

    global tables
    global metadata

    data = tables.get(table)
    meta_cols = metadata.get(table).get("cols")
    row_cnt = 0

    # delete from list tail
    for i in range(len(data) - 1, -1, -1):
        if can_be_filter(data[i], meta_cols, filters):
            del data[i]
            row_cnt += 1

    tables[table] = data
    flush_table(table)

    print("delete {} rows".format(row_cnt))


def upd_executor(*args, **kwargs):
    """
    update specified table
    :param table:
    :param chgset:
    :param filters:
    :return:
    """

    table = kwargs.get("table")
    chgset = kwargs.get("chgset")
    filters = kwargs.get("filters")

    global tables
    global metadata
    data = tables.get(table)
    meta_cols = metadata.get(table).get("cols")
    row_cnt = 0

    def update_row(row, chgset):
        """
        update row based on change set
        :param row: row list
        :param chgset: change set (ex: set a=1,b=2)
        :return: updated row
        """
        for ch in chgset:
            ind = meta_cols.index(ch[0])
            row[ind] = ch[2]
        return row

    # update row
    for i, row in enumerate(data):
        if can_be_filter(data[i], meta_cols, filters):
            update_row(data[i], chgset)
            row_cnt += 1

    tables[table] = data
    flush_table(table)

    print("update {} rows".format(row_cnt))


def find_executor(*args, **kwargs):
    """
    find executor
    :param args:
    :param kwargs:
    :return:
    """

    table = kwargs.get("table")
    columns = kwargs.get("columns")
    filters = kwargs.get("filters")

    global tables
    global metadata
    data = tables.get(table)
    meta_cols = metadata.get(table).get("cols")
    row_cnt = 0

    # print row based on metadata and columns
    def print_row(row, meta, columns):
        """
        print row based on metadata and columns
        :param row: row list
        :param meta: metadata
        :param columns: column names
        :return:
        """
        for col in columns:
            ind = meta.index(col)
            print("{:<20}".format(row[ind]), end="")
        print("\n", end="")

    # print table head
    print_row(meta_cols, meta_cols, columns)
    print("")
    for row in data:
        # print result
        if can_be_filter(row, meta_cols, filters):
            print_row(row, meta_cols, columns)
            row_cnt += 1

    print("find {} rows".format(row_cnt))


load_table("staff_table")
while True:
    sql = input("SQL>").strip()
    sql_parser(sql)
