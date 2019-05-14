import operator
import json

from bean.BaseInfo import BaseInfo
from db.MapperExecute import MapperExecute
from util import MD5
from util.Logger import Logger
from util.Redis import Redis

REDIS_KEY_SET_NAME = 'REDIS_KEY_SET'
REDIS_HASH_KEY_PREFIX = 'REDIS_HASH_'

MYSQL_KEY_SET_NAME = 'MYSQL_KEY_SET'
MYSQL_HASH_KEY_PREFIX = 'MYSQL_HASH_'

logger = Logger()


def write_to_redis(_data):
    """
    向Redis中写数据
    TODO
    :param _data: 单条Json格式数据
    :return:
    """
    redis = Redis()
    redis.set(_data['coding'], _data)


def write_to_mysql(_data):
    """
    向Mysql中写数据
    :param _data: 单条Json格式数据
    :return:
    """
    redis = Redis().get_instance()
    _id = _data['coding']
    redis_hash_key = REDIS_HASH_KEY_PREFIX + _id
    mysql_hash_key = MYSQL_HASH_KEY_PREFIX + _id

    hash_value = _id + MD5.obj_md5(_data)

    redis.set(_id, json.dumps(_data))  # redis中的对象
    redis.set(redis_hash_key, hash_value)  # redis中对象的特征值

    __m_exe = MapperExecute()
    if redis.exists(mysql_hash_key):
        if operator.eq(redis.get(mysql_hash_key), hash_value):
            ret = __m_exe.update_by_pk(BaseInfo(), _data)
            logger.info('更新影响行数：' + str(ret) + '[' + _id + ']')
        else:
            logger.debug('数据库与爬取内容相同：' + '[' + _id + ']:' + str(_data))
    else:
        __m_exe.insert_selective(BaseInfo(), _data)
        logger.info('新增项数据：' + '[' + _id + ']')
    redis.set(mysql_hash_key, hash_value)
