class Where:
    """
    查询条件
    """
    # 查询字段名
    __field = None
    # 查询表达式
    __express = None
    # 字段值
    __value = None

    def __init__(self, _field, _express, _value):
        self.__field = _field
        self.__express = _express
        self.__value = _value

    def get_field(self):
        return self.__field

    def get_express(self):
        return self.__express

    def get_value(self):
        return self.__value
