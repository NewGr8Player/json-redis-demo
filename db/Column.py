# Column
class Column:
    # 字段名
    __name = ""
    # 字段类型
    __type = None
    # 是否主键
    __pk = False

    # 初始化方法
    def __init__(self, _name, _type=str.__name__, pk=False):
        self.__name = _name
        self.__type = _type
        self.__pk = pk

    def get_name(self):
        return self.__name;

    def get_typ(self):
        return self.__type

    def is_pk(self):
        return self.__pk
