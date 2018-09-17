import json
import operator
import time
from random import randint

import requests
from requests import RequestException

from util import Config
from work.work import write_to_mysql

# 基础路径
base_url = Config.config_getter('base_url')
# 空数据对象
EMPTY_DATA_OBJECT = {"total": 0, "rows": []}


# 构造url
def url_constractor(_current, _page_size):
    return base_url + '?limit=' + str(_page_size) + '&offset=' + str(_current)


# 获取数据
def data_getter(url):
    try:
        response = requests.get(url)
        if operator.eq(response.status_code, 200):
            ret = response.text  # 不要使用content，content内容为byte，还要转码
            return json.loads(ret, encoding='utf-8')
        else:
            print('返回错误码:' + str(response.status_code))
            return EMPTY_DATA_OBJECT
    except RequestException:
        return EMPTY_DATA_OBJECT


# 分析数据
def data_analyzer(_data_list):
    if int(_data_list['total']) > 0:
        for _data in _data_list['rows']:
            write_to_mysql(_data)


# 保存到数据库
def save_to_db(_data):
    return write_to_mysql(_data)


# 循环获取
def looper(current_index=1, page_size=100):
    while current_index > 0:
        data_analyzer(data_getter(url_constractor(current_index, page_size)))
        current_index += 1
        random_sleep()


# 随机防Ban
def random_sleep():
    sleep_time = (
                         randint(0, 9) * 100 +
                         randint(0, 9) * 10 +
                         randint(0, 9)
                 ) / 1000
    print('防ban休眠:' + str(sleep_time), end='')
    time.sleep(sleep_time)
    print('====结束休眠')


# 程序入口
if __name__ == '__main__':
    looper(1, 10000)
