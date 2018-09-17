import pymysql
from util import Config

__host = Config.mysql_getter("mysql_host")
__user = Config.mysql_getter("mysql_user")
__passwd = Config.mysql_getter("mysql_passwd")
__db = Config.mysql_getter("mysql_db")
__port = int(Config.mysql_getter("mysql_port"))
__charset = Config.mysql_getter("mysql_charset")


# 执行查询，返回数据
def execute(sql_str):
    if sql_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(sql_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = pymysql.connect(host=__host, user=__user, passwd=__passwd, db=__db,
                               port=__port, charset=__charset)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql_str)
        data = cur.fetchall()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except Exception as e:
        raise e


# 插入数据，返回数据主键
def execute_insert(insert_str, data):
    if insert_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(insert_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = pymysql.connect(host=__host, user=__user, passwd=__passwd, db=__db,
                               port=__port, charset=__charset)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(insert_str, data)
        # data = cur.fetchall()
        # last_id = cur.lastrowid
        last_id = conn.insert_id()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return last_id
    except Exception as e:
        raise e


# 更新数据，返回更新条数
def execute_update(update_str, data):
    if update_str is None:
        raise Exception("参数不能为空：update_str")
    if len(update_str) == 0:
        raise Exception("参数不能为空：update_str")
    try:
        conn = pymysql.connect(host=__host, user=__user, passwd=__passwd, db=__db,
                               port=__port, charset=__charset)
        cur = conn.cursor()  # 获取一个游标
        count = cur.execute(update_str, data)
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return count
    except Exception as e:
        raise e


# 执行带参数的查询，返回查询结果
def execute_select(select_str, data):
    if select_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(select_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = pymysql.connect(host=__host, user=__user, passwd=__passwd, db=__db,
                               port=__port, charset=__charset)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(select_str, data)
        data = cur.fetchall()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except Exception as e:
        raise e


# 执行带参数的删除
def execute_delete(select_str, data):
    if select_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(select_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        conn = pymysql.connect(host=__host, user=__user, passwd=__passwd, db=__db,
                               port=__port, charset=__charset)
        cur = conn.cursor()  # 获取一个游标
        cur.execute(select_str, data)
        data = cur.fetchall()
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except Exception as e:
        raise e
