import configparser
import os
from xml.etree import ElementTree as ElementTree
from xlrd import open_workbook

class util:
    cf = configparser.ConfigParser()

    def get_config(self, abspath, section, key):
        """
        获取配置文件中的值
        :param abspath:
        :param section:
        :param key:
        :return:
        """
        filePath = os.path.abspath(abspath)
        self.cf.read(filePath, encoding="UTF-8")
        return self.cf.get(section, key)

    # 从excel中读取测试数据
    def get_xls(xls_name,sheet_name):
        cls=[]
        xlsPath=os.path.join(os.path.realpath("../TestData"), xls_name)
        print(xlsPath)
        file=open_workbook(xlsPath,encoding_override='utf-8')
        sheet=file.sheet_by_name(sheet_name)
        print(sheet)
        nrows=sheet.nrows
        print(nrows)
        for i in range(nrows):
            if sheet.row_values(i)[0] !=u'case_name':
                cls.append(sheet.row_values(i))
        return cls

    # 读取xml语句存储在字典中
    def set_xml(self):
        database = {}
        if len(database) == 0:
            sql_path = os.path.join('E:\\python_lianxi\\APITest\\testFile', "sql.xml")
            tree = ElementTree.parse(sql_path)
            for db in tree.findall("database"):
                db_name = db.get("name")
                # print(db_name)
                table = {}
                ss = list(db)
                for tb in ss:
                    table_name = tb.get("name")
                    # print(table_name)
                    sql = {}
                    sss = list(tb)
                    for data in sss:
                        sql_id = data.get("id")
                        # print(sql_id)
                        sql[sql_id] = data.text
                    table[table_name] = sql
                database[db_name] = table
            # print(database)
        return database


    # 获取sql语句
    def get_sql(self ,database_name, table_name, sql_id):
        database=self.set_xml()
        sql_ele = database.get(database_name).get(table_name).get(sql_id)
        sql= str(sql_ele).replace('  ','',60)
        return sql


if __name__=="__main__":
    s=util().get_sql('new111','table000','select_num')

    print(s)
