from db.Condition import Condition
from util import DataBase
import operator


class BaseMapper:
    """
    数据库基础操作封装
    """

    def get_data_val(self, data, col):
        """
        从data中获取指定名字的数据，名字不兼容大小写
        :param data: 数据对象
        :param col: 数据列
        :return:
        """
        if data is None:
            return None
        if col is None:
            return None
        val_name = None
        if operator.eq(type(col).__name__, 'str'):
            val_name = col
        if operator.eq(type(col).__name__, 'Column'):
            val_name = col.get_name()
        if val_name is None or len(val_name) == 0:
            return None
        try:
            return data[val_name]
        except Exception as e:
            return None

    def join_col(self, cols):
        """
        拼接列名
        :param cols: 数据列
        :return:
        """
        if cols is None:
            return '*'
        if len(cols) == 0:
            return '*'
        col_strs = []
        for col in cols:

            if operator.eq(type(col).__name__, 'str'):
                col_strs.append(col)
            if operator.eq(type(col).__name__, "Column"):
                col_strs.append(col.get_name())
        return ','.join(col_strs)

    def get_pk(self, cols):
        """
        从多列中找到主键列
        :param cols: 数据列
        :return:
        """
        t_pk = 'ID'
        if cols is None:
            return t_pk
        if len(cols) == 0:
            return t_pk
        for col in cols:
            if operator.eq(type(col).__name__, 'Column'):
                if col.is_pk:
                    return col.get_name()
        t_pk = cols[0]
        return t_pk

    def b_select_by_pk(self, table_name, cols, pk):
        """
        按主键查询
        :param table_name: 表名
        :param cols: 数据列
        :param pk: 主键值
        :return:
        """
        if table_name is None:
            raise Exception('参数异常：table_name')
        if len(table_name) == 0:
            raise Exception('参数异常：table_name')
        if pk is None:
            raise Exception('参数异常：pk')

        cols_str = self.join_col(cols)
        t_pk = self.get_pk(cols)
        sql = 'select ' + cols_str + ' from ' + table_name + ' where ' + t_pk + ' = ' + str(pk)
        sel_data = DataBase.execute(sql)
        if sel_data is None or len(sel_data) == 0 or len(sel_data[0]) == 0:
            return None
        row_data = sel_data[0]
        if row_data is None or len(row_data) == 0:
            return None
        row_dic = {}
        col_strs = []
        for col in cols:
            if operator.eq(type(col).__name__, 'str'):
                col_strs.append(col)
            if operator.eq(type(col).__name__, 'Column'):
                col_strs.append(col.get_name())
        ind = 0
        for col_st in col_strs:
            row_dic[col_st] = row_data[ind]
            ind = ind + 1
        return row_dic

    def b_delete_by_pk(self, table_name, pk_name, pk):
        """
        按主键删除
        :param table_name: 表名
        :param pk_name: 主键名
        :param pk: 主键值
        :return:
        """
        if table_name is None:
            raise Exception('参数异常：table_name')
        if len(table_name) == 0:
            raise Exception('参数异常：table_name')
        if pk_name is None:
            raise Exception('参数异常：pk_name')
        if len(pk_name) == 0:
            raise Exception('参数异常：pk_name')
        if pk is None:
            raise Exception('参数异常：pk')

        sql = 'delete from ' + table_name + ' where ' + pk_name + ' = ' + str(pk)
        del_data = DataBase.execute(sql)
        return del_data

    def b_insert(self, table_name, cols, data):
        """
        插入（不判空），并返回主键
        :param table_name: 表名
        :param cols: 全部数据列
        :param data: 待插入数据
        :return:
        """
        t_sql = 'insert into ' + table_name + '('
        col_strs = []
        hol_strs = []
        val_strs = []
        for col in cols:
            col_name = ''
            if type(col).__name__ == 'Column':
                col_name = col.get_name()
            else:
                col_name = col
            if len(col_name) == 0:
                continue
            col_strs.append(col_name)
            hol_strs.append('%s')
            val = self.get_data_val(data, col_name)
            val_strs.append(val)

        col_len = len(col_strs)

        if col_len == 0:
            raise Exception('没有任何列')
        col_str = ','.join(col_strs)
        hol_str = ','.join(hol_strs)
        t_sql = t_sql + col_str + ') values (' + hol_str + ')'
        ins_pk = DataBase.execute_insert(t_sql, val_strs)
        return ins_pk

    def b_insert_selective(self, table_name, cols, data):
        """
        插入（判空），并返回主键
        :param table_name: 表名
        :param cols: 全部数据列
        :param data: 待插入数据
        :return:
        """
        t_sql = 'insert into ' + table_name + '('
        col_strs = []
        hol_strs = []
        val_strs = []
        for col in cols:
            col_name = ''
            if type(col).__name__ == 'Column':
                col_name = col.get_name()
            else:
                col_name = col
            if len(col_name) == 0:
                continue
            val = self.get_data_val(data, col_name)
            if val is None:
                continue
            col_strs.append(col_name)
            hol_strs.append('%s')
            val_strs.append(val)

        col_len = len(col_strs)

        if col_len == 0:
            raise Exception('没有任何列')
        col_str = ','.join(col_strs)
        hol_str = ','.join(hol_strs)
        t_sql = t_sql + col_str + ') value (' + hol_str + ')'
        ins_pk = DataBase.execute_insert(t_sql, val_strs)
        return ins_pk

    def b_update_by_pk(self, table_name, cols, data):
        """
        按主键更新
        :param table_name: 表名
        :param cols: 全部数据列
        :param data: 待更新数据
        :return:
        """
        t_pk = self.get_pk(cols)
        if t_pk is None or len(t_pk) == 0:
            raise Exception('未找到主键')

        pk_val = self.get_data_val(data, t_pk)
        if pk_val is None:
            raise Exception('未找到主键值')

        col_strs = []
        val_strs = []
        for col in cols:
            col_name = ''
            if type(col).__name__ == 'Column':
                col_name = col.get_name()
            else:
                col_name = col
            if len(col_name) == 0:
                continue
            if t_pk == col_name:
                continue

            val = self.get_data_val(data, col_name)
            val_strs.append(val)
            col_s = col_name + '=%s'
            col_strs.append(col_s)

        col_str = ','.join(col_strs)
        val_strs.append(pk_val)
        t_sql = 'update ' + table_name + ' set ' + col_str + ' where ' + t_pk + ' =%s'
        count = DataBase.execute_update(t_sql, val_strs)
        return count

    def b_update_by_pk_selective(self, table_name, cols, data):
        """
        按主键更新（空字段不更新）
        :param table_name: 表名
        :param cols: 全部数据列
        :param data: 待更新数据
        :return:
        """
        t_pk = self.get_pk(cols)
        if t_pk is None or len(t_pk) == 0:
            raise Exception('未找到主键')

        pk_val = self.get_data_val(data, t_pk)
        if pk_val is None:
            raise Exception('未找到主键值')

        col_strs = []
        val_strs = []
        for col in cols:
            col_name = ''
            if type(col).__name__ == 'Column':
                col_name = col.get_name()
            else:
                col_name = col
            if len(col_name) == 0:
                continue
            if t_pk == col_name:
                continue

            val = self.get_data_val(data, col_name)
            if val is None:
                continue
            val_strs.append(val)
            col_s = col_name + '=%s'
            col_strs.append(col_s)

        col_str = ','.join(col_strs)
        val_strs.append(pk_val)
        t_sql = 'update ' + table_name + ' set ' + col_str + ' where ' + t_pk + ' =%s'
        count = DataBase.execute_update(t_sql, val_strs)
        return count

    def b_select_by_condition(self, table_name, cols, condition_tuple):
        """
        按条件查询
        :param table_name: 表名
        :param cols: 全部数据列
        :param condition_tuple: 查询条件
        :return:
        """
        cond = Condition(condition_tuple)
        if table_name is None:
            raise Exception('参数异常：table_name')
        if len(table_name) == 0:
            raise Exception('参数异常：table_name')
        where_sql = cond.get_sql()
        vals = cond.get_vals()
        cols_str = self.join_col(cols)
        sql = 'select ' + cols_str + ' from ' + table_name + ' where ' + where_sql
        sel_data = DataBase.execute_select(sql, vals)
        if sel_data is None or len(sel_data) == 0:
            return None
        row_datas = sel_data
        if row_datas is None or len(row_datas) == 0:
            return None
        col_strs = []
        for col in cols:
            if type(col).__name__ == 'str':
                col_strs.append(col)
            if type(col).__name__ == 'Column':
                col_strs.append(col.get_name())
        row_dics = []
        for row_data in row_datas:
            row_dic = {}
            ind = 0
            for col_st in col_strs:
                row_dic[col_st] = row_data[ind]
                ind = ind + 1
            row_dics.append(row_dic)
        return row_dics

    def b_delete_by_condition(self, table_name, condition_tuple):
        """
        按条件删除
        :param table_name: 表名
        :param condition_tuple: 删除条件
        :return:
        """
        cond = Condition(condition_tuple)
        if table_name is None:
            raise Exception('参数异常：table_name')
        if len(table_name) == 0:
            raise Exception('参数异常：table_name')
        where_sql = cond.get_sql()
        vals = cond.get_vals()
        sql = 'delete from ' + table_name + ' where ' + where_sql
        return DataBase.execute_delete(sql, vals)

    def b_count_by_condition(self, table_name, condition_tuple):
        """
        按条件查询统计数量
        :param table_name: 表名
        :param condition_tuple: 统计条件
        :return:
        """
        cond = Condition(condition_tuple)
        if table_name is None:
            raise Exception('参数异常：table_name')
        if len(table_name) == 0:
            raise Exception('参数异常：table_name')
        where_sql = cond.get_sql()
        vals = cond.get_vals()
        sql = 'select count(1) from ' + table_name + ' where ' + where_sql
        datas = DataBase.execute_delete(sql, vals)
        if datas is None or len(datas) == 0:
            return 0
        data = datas[0]
        if data is None:
            return 0
        return int(data[0])
