import hashlib
import json


def str_md5(_str):
    """
    字符串MD5
    :param _str:字符串
    :return:字符串的MD5值
    """
    m = hashlib.md5()
    m.update(_str.encode())
    return m.hexdigest()


def obj_md5(_obj):
    """
    对象的MD5
    :param _obj:对象
    :return:字符串的MD5值
    """
    return str_md5(json.dumps(_obj))
