import redis
from util import Config


# Redis 工具类
class Redis:
    __pool = None

    def __init__(self):
        self.__pool = redis.ConnectionPool(
            host=Config.redis_getter("redis_host"),
            password=Config.redis_getter("redis_passwd"),
            port=int(Config.redis_getter("redis_port")),
            db=3)

    # 使用Redis连接池操作
    def get_instance(self):
        return redis.Redis(connection_pool=self.__pool)
