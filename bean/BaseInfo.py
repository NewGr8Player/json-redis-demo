from db.Column import Column


class BaseInfo:
    """
    基础数据信息Bean
    """
    # 数据表字段
    __cols = [
        Column("coding", str.__name__, True),
        Column("farmersName"),
        Column("species"),
        Column("number"),
        Column("name"),
        Column("phone"),
        Column("address"),
        Column("positioningAddresss"),
        Column("qrcode"),
        Column("scale"),
        Column("user"),
        Column("amNumber"),
        Column("username"),
        Column("splog"),
        Column("label"),
        Column("allQrcode"),
        Column("label2"),
        Column("admin"),
        Column("recordNumber")
    ]

    # 数据表名
    __name = "t_basic_info"

    def get_name(self):
        return self.__name

    def get_cols(self):
        return self.__cols
