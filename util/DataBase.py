from util.DataBasePool import DataBasePool

POOL = DataBasePool()


# 插入数据，返回数据主键
def execute_insert(insert_str, data):
    if insert_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(insert_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        POOL.execute_sql(insert_str, data)
    except Exception as e:
        raise e


# 更新数据，返回更新条数
def execute_update(update_str, data):
    if update_str is None:
        raise Exception("参数不能为空：update_str")
    if len(update_str) == 0:
        raise Exception("参数不能为空：update_str")
    try:
        return POOL.execute_sql(update_str, data)
    except Exception as e:
        raise e


# 执行带参数的查询，返回查询结果
def execute_select(select_str, data):
    if select_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(select_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        return POOL.execute_query(select_str, data)
    except Exception as e:
        raise e


# 执行带参数的删除
def execute_delete(select_str, data):
    if select_str is None:
        raise Exception("参数不能为空：sql_str")
    if len(select_str) == 0:
        raise Exception("参数不能为空：sql_str")
    try:
        return POOL.execute_sql(select_str, data)
    except Exception as e:
        raise e
