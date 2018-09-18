from util.DataBasePool import DataBasePool

from util.Logger import Logger

# 数据库连接池实例
POOL = DataBasePool()
logger = Logger()


def execute_insert(insert_str, data):
    """
    执行插入语句
    :param insert_str:插入语句
    :param data:数据
    :return:影响行数
    """
    if insert_str is None or len(insert_str) == 0:
        info = "参数不能为空：sql_str"
        logger.error(info)
        raise Exception(info)
    try:
        return POOL.execute_sql(insert_str, data)
    except Exception as e:
        logger.error(str(e))
        raise e


def execute_update(update_str, data):
    """
    执行更新语句
    :param update_str: 更新语句
    :param data: 数据
    :return: 影响行数
    """
    if update_str is None or len(update_str) == 0:
        info = "参数不能为空：update_str"
        logger.error(info)
        raise Exception(info)
    try:
        return POOL.execute_sql(update_str, data)
    except Exception as e:
        logger.error(str(e))
        raise e


def execute_select(select_str, data):
    """
    执行查询语句
    :param select_str: 查询语句
    :param data: 条件数据
    :return: 结果集
    """
    if select_str is None or len(select_str) == 0:
        info = "参数不能为空：sql_str"
        logger.error(info)
        raise Exception(info)
    try:
        return POOL.execute_query(select_str, data)
    except Exception as e:
        logger.error(str(e))
        raise e


def execute_delete(delete_str, data):
    """
    执行删除语句
    :param delete_str: 删除语句
    :param data: 删除条件
    :return: 影响行数
    """
    if delete_str is None or len(delete_str) == 0:
        info = "参数不能为空：sql_str"
        logger.error(info)
        raise Exception(info)
    try:
        return POOL.execute_sql(delete_str, data)
    except Exception as e:
        logger.error(str(e))
        raise e
