import hashlib
import json


# 字符串MD5
def str_md5(_str):
    m = hashlib.md5()
    m.update(_str.encode())
    return m.hexdigest()


# 对象MD5
def obj_md5(_obj):
    return str_md5(json.dumps(_obj))
