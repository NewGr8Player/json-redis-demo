from db.BaseMapper import BaseMapper


class MapperExecute:
    """
    Sql执行器
    """
    __mapper = None

    def __init__(self):
        self.__mapper = BaseMapper()

    def select_by_pk(self, cfg, pk):
        """
        按主键查询
        :param cfg: 表配置
        :param pk: 主键值
        :return:
        """
        pk_data = self.__mapper.b_select_by_pk(cfg.get_name(), cfg.get_cols(), pk)
        return pk_data

    def delete_by_pk(self, cfg, pk):
        """
        按主键删除
        :param cfg: 表配置
        :param pk: 主键值
        :return:
        """
        t_pk = self.__mapper.get_pk(cfg.get_cols())
        del_data = self.__mapper.b_delete_by_pk(cfg.get_name(), t_pk, pk)
        return del_data

    def insert(self, cfg, par_data):
        """
        插入
        :param cfg: 表配置
        :param par_data: 待插入的数据
        :return:
        """
        t_pk = self.__mapper.b_insert(cfg.get_name(), cfg.get_cols(), par_data)
        return t_pk

    def insert_selective(self, cfg, par_data):
        """
        插入
        :param cfg: 表配置
        :param par_data: 待插入的数据
        :return:
        """
        t_pk = self.__mapper.b_insert_selective(cfg.get_name(), cfg.get_cols(), par_data)
        return t_pk

    def update_by_pk(self, cfg, par_data):
        """
        按主键更新
        :param cfg: 表配置
        :param par_data: 待更新的数据
        :return:
        """
        count = self.__mapper.b_update_by_pk(cfg.get_name(), cfg.get_cols(), par_data)
        return count

    # 按主键更新
    # cfg 表配置
    # par_data 待更新的数据
    def update_by_pk_selective(self, cfg, par_data):
        count = self.__mapper.b_update_by_pk_selective(cfg.get_name(), cfg.get_cols(), par_data)
        return count

    def select_by_condition(self, cfg, condition_tuple):
        """
        按条件查询
        :param cfg: 表配置
        :param condition_tuple: 查询条件
        :return:
        """
        datas = self.__mapper.b_select_by_condition(cfg.get_name(), cfg.get_cols(), condition_tuple)
        return datas

    def delete_by_condition(self, cfg, condition_tuple):
        """
        按条件删除
        :param cfg: 表配置
        :param condition_tuple: 删除条件
        :return:
        """
        datas = self.__mapper.b_delete_by_condition(cfg.get_name(), condition_tuple)
        return datas

    def count_by_condition(self, cfg, condition_tuple):
        """
        按条件统计
        :param cfg: 表配置
        :param condition_tuple: 统计条件
        :return:
        """
        count_c = self.__mapper.b_count_by_condition(cfg.get_name(), condition_tuple)
        return count_c
