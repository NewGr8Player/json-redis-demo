import configparser
import os

__path = os.getcwd()
__conf_file = __path + os.path.sep + 'config.ini'
__config_section = 'config'
__redis_section = 'redis'
__mysql_section = 'mysql'
__log_section = 'log'

conf = configparser.ConfigParser()
conf.read(__conf_file)


def config_getter(name):
    """
    Config命名空间下配置获取
    :param name: 配置项名称
    :return: 配置项值
    """
    val = conf.get(__config_section, name)
    return val


def redis_getter(name):
    """
    Redis命名空间下配置获取
    :param name: 配置项名称
    :return: 配置项值
    """
    val = conf.get(__redis_section, name)
    return val


def mysql_getter(name):
    """
    Mysql命名空间下配置获取
    :param name: 配置项名称
    :return: 配置项值
    """
    val = conf.get(__mysql_section, name)
    return val


def log_getter(name):
    val = conf.get(__log_section, name)
    return val
