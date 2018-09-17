# Order 排序
class Order:
    # 排序字段
    __field = None
    # 排序方向
    __order = "ASC"

    def __init__(self, _field, _order):
        self.__field = _field
        self.__order = _order

    def get_field(self):
        return self.__field

    def get_order(self):
        return self.__order
