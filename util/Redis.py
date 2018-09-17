import redis
from util import Config


# Redis 工具类
class Redis:
    __pool = None

    def __init__(self):
        __host = Config.get_redis("redis_host")
        __port = int(Config.get_redis("redis_port"))
        self.__pool = redis.ConnectionPool(host=__host, port=__port)

    # 保存数据
    def r_set(self, key, value, expire=None):
        redi = redis.Redis(connection_pool=self.__pool)
        redi.set(key, value, ex=expire)

    # 获取数据
    def r_get(self, key):
        redi = redis.Redis(connection_pool=self.__pool)
        value = redi.get(key)
        if value is None:
            return None
        value = value.decode(Config.get_redis('redis_charset'))
        return value

    # 删除数据
    def r_del(self, key):
        redi = redis.Redis(connection_pool=self.__pool)
        redi.delete(key)
