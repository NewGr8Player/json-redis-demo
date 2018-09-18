import pymysql
from DBUtils.PooledDB import PooledDB
from pymysql.cursors import DictCursor

from util import Config
from util.Logger import Logger

logger = Logger()


# 数据库连接池
class DataBasePool(object):
    # 连接池对象
    __pool = None

    def __init__(self):
        self.__pool = PooledDB(creator=pymysql, mincached=1, maxcached=20,
                               host=Config.mysql_getter("mysql_host"),
                               port=int(Config.mysql_getter("mysql_port")),
                               user=Config.mysql_getter("mysql_user"),
                               passwd=Config.mysql_getter("mysql_passwd"),
                               db=Config.mysql_getter("mysql_db"),
                               use_unicode=False,
                               charset=Config.mysql_getter("mysql_charset"),
                               cursorclass=DictCursor)

    def execute_query(self, sql, args=()):
        """
        执行查询语句，获取结果
        :param sql:sql语句，注意防注入
        :param args:传入参数
        :return:结果集
        """
        result = ()
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            logger.info(sql)
            logger.info(args)
            cur.execute(sql, args)
            result = cur.fetchall()
        except Exception as e:
            logger.info('异常信息:' + str(e))
        cur.close()
        conn.close()
        return result

    def execute_query_single(self, sql, args=()):
        """
        执行查询语句，获取单行结果
        :param sql:sql语句，注意防注入
        :param args:传入参数
        :return:结果集
        """
        result = ()
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            logger.info(sql)
            logger.info(args)
            cur.execute(sql, args)
            result = cur.fetchone()
        except Exception as e:
            logger.error('异常信息:' + str(e))
        cur.close()
        conn.close()
        return result

    def execute_sql(self, sql, args=()):
        """
        执行增删改语句
        :param sql:sql语句，注意防注入
        :param args:传入参数
        :return:影响行数,mysql和sqlite有返回值
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            logger.info(sql)
            logger.info(args)
            result = cur.execute(sql, args)
            conn.commit()
            count = result
        except Exception as e:
            logger.error('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count

    def execute_many_sql(self, sql, args):
        """
        批量执行增删改语句
        :param sql:sql语句，注意防注入
        :param args:参数,内部元组或列表大小与sql语句中参数数量一致
        :return:影响行数，mysql和sqlite有返回值
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            logger.info(sql)
            logger.info(args)
            result = cur.executemany(sql, args)
            conn.commit()
            count = result
        except Exception as e:
            logger.error('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count
