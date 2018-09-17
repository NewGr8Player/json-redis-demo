from requests import RequestException

from bean.BaseInfo import BaseInfo
from db.MapperExecute import MapperExecute
from util import Config
import json
import requests

# 基础路径
base_url = Config.config_getter('base_url')


# 构造url
def url_constractor(_current, _page_size):
    return base_url + '?limit=' + str(_page_size) + '&offset=' + str(_current)


# 获取数据
def data_getter(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            ret = response.text  # 不要使用content，content内容为byte，还要转码
            return json.loads(ret, encoding='utf-8')
    except RequestException:
        return None


# 分析数据
def data_analyzer(_data):
    if _data:
        print()


# 保存到数据库
def save_to_db():
    print()


# 程序入口
if __name__ == '__main__':
    # main method
    data = data_getter(url_constractor(1, 10))
    print(data)
    print(len(data['rows']))

    # 执行工具
    __m_exe = MapperExecute()
    # 表配置
    __user_cfg = BaseInfo()
    # 待插入数据
    user_info = data['rows'][0]
    # 执行插入
    __m_exe.insert_selective(__user_cfg, user_info)
