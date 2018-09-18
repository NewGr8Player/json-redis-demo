class Page:
    """
    分页
    """
    # 页码，从1开始，默认1
    __page = 1
    # 分页大小，默认20
    __size = 20

    def __init__(self, _page, _size):
        self.__page = _page
        self.__size = _size

    def get_offset(self):
        pag = self.__page
        siz = self.__size
        off = (pag - 1) * siz
        return off

    def get_size(self):
        return self.__size
