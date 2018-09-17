from db.BaseMapper import BaseMapper


# MapperExecute
class MapperExecute:
    __mapper = None

    def __init__(self):
        self.__mapper = BaseMapper()

    # 按主键查询
    # cfg 表配置
    # pk 主键值
    def select_by_pk(self, cfg, pk):
        pk_data = self.__mapper.b_select_by_pk(cfg.get_name(), cfg.get_cols(), pk)
        return pk_data

    # 按主键删除
    # cfg 表配置
    # pk 主键值
    def delete_by_pk(self, cfg, pk):
        t_pk = self.__mapper.get_pk(cfg.get_cols())
        del_data = self.__mapper.b_delete_by_pk(cfg.get_name(), t_pk, pk)
        return del_data

    # 插入
    # cfg 表配置
    # par_data 待插入的数据
    def insert(self, cfg, par_data):
        t_pk = self.__mapper.b_insert(cfg.get_name(), cfg.get_cols(), par_data)
        return t_pk

    # 插入
    # cfg 表配置
    # par_data 待插入的数据
    def insert_selective(self, cfg, par_data):
        t_pk = self.__mapper.b_insert_selective(cfg.get_name(), cfg.get_cols(), par_data)
        return t_pk

    # 按主键更新
    # cfg 表配置
    # par_data 待更新的数据
    def update_by_pk(self, cfg, par_data):
        count = self.__mapper.b_update_by_pk(cfg.get_name(), cfg.get_cols(), par_data)
        return count

    # 按主键更新
    # cfg 表配置
    # par_data 待更新的数据
    def update_by_pk_selective(self, cfg, par_data):
        count = self.__mapper.b_update_by_pk_selective(cfg.get_name(), cfg.get_cols(), par_data)
        return count

    # 按条件查询
    # cfg 表配置
    # condition_tuple 查询条件
    def select_by_condition(self, cfg, condition_tuple):
        datas = self.__mapper.b_select_by_condition(cfg.get_name(), cfg.get_cols(), condition_tuple)
        return datas

    # 按条件删除
    # cfg 表配置
    # condition_tuple 删除条件
    def delete_by_condition(self, cfg, condition_tuple):
        datas = self.__mapper.b_delete_by_condition(cfg.get_name(), condition_tuple)
        return datas

    # 按条件统计
    # cfg 表配置
    # condition_tuple 统计条件
    def count_by_condition(self, cfg, condition_tuple):
        count_c = self.__mapper.b_count_by_condition(cfg.get_name(), condition_tuple)
        return count_c
