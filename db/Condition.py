# Condition 条件解析
class Condition:
    # 解析后的sql语句
    __sql = None
    # 解析后的条件值
    __vals = None

    def __init__(self, _condition):
        # 解析sql语句
        sql_s = ana_condition_sql(_condition, "")
        if sql_s is None:
            self.__sql = None
        else:  # 需要删除前后的括号“()”
            sql_len = len(sql_s)
            if sql_len <= 2:
                self.__sql = None
            else:
                if sql_s.startswith("("):
                    sql_s = sql_s[1:sql_len - 1]
        self.__sql = sql_s
        # 解析条件值
        self.__vals = ana_condition_val(_condition, [])

    def get_sql(self):
        return self.__sql

    def get_vals(self):
        return self.__vals


# 递归解析sql语句
# 最外层的“condition”是个tuple
def ana_condition_sql(_condition, _sql):
    # 条件单元
    if type(_condition).__name__ == "Qwhere":
        if _condition.get_field() is None or _condition.get_express() is None or _condition.get_value() is None:
            return _sql
        ss = _condition.get_field() + " " + _condition.get_express() + " %s"
        _sql = _sql + ss + " "
        return _sql
    # 排序单元
    if type(_condition).__name__ == "Qorder":
        if _condition.get_field() is None or _condition.get_order() is None:
            return _sql
        ss = " order by " + _condition.get_field() + " " + _condition.get_order() + ""
        _sql = _sql + ss + " "
        return _sql
    # 分页单元
    if type(_condition).__name__ == "Qpage":
        if _condition.get_offset() is None or _condition.get_size() is None:
            return _sql
        ss = " limit " + str(_condition.get_offset()) + "," + str(_condition.get_size()) + ""
        _sql = _sql + ss + " "
        return _sql
    # 连接字符串（=，>，< 等）
    if type(_condition).__name__ == "str":
        _sql = _sql + " " + _condition + " "
        return _sql
    if type(_condition).__name__ == "tuple":
        _sql = _sql + "("
        for __con in _condition:
            _sql = ana_condition_sql(__con, _sql)
        _sql = _sql + ")"
        return _sql
    return _sql


# 递归解析sql查询值
def ana_condition_val(_condition, _vals):
    if type(_condition).__name__ == "Qwhere":
        if _condition.get_field() is None or _condition.get_express() is None or _condition.get_value() is None:
            return _vals
        _vals.append(_condition.get_value())
        return _vals
    if type(_condition).__name__ == "tuple":
        for __con in _condition:
            _vals = ana_condition_val(__con, _vals);
        return _vals
    return _vals
