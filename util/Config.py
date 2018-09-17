import configparser
import os

__path = os.getcwd()
__conf_file = __path + os.path.sep + "config.ini"
__config_section = "config"
__redis_section = "redis"
__mysql_section = "mysql"

conf = configparser.ConfigParser()
conf.read(__conf_file)


# Config命名空间下配置获取
def config_getter(name):
    val = conf.get(__config_section, name)
    return val


# Redis命名空间下配置获取
def redis_getter(name):
    val = conf.get(__redis_section, name)
    return val


# Mysql命名空间下配置获取
def mysql_getter(name):
    val = conf.get(__mysql_section, name)
    return val
