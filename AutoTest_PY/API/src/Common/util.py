import configparser
import os
from xml.etree import ElementTree as ElementTree

from xlrd import open_workbook


class util:

    def __init__(self):
        self.configPath = os.path.abspath("../../config.ini")
        self.testCaseExcelPath = os.path.abspath("../TestData/file/login.xls")
        self.sqlXmlPath = os.path.abspath("../TestData/file/sql.xml")
        self.conf = configparser.ConfigParser()
        self.conf.read(self.configPath, encoding='utf-8')

    def get_user(self, key):
        """
        读取配置文件用户用户信息
        :param key:
        :return:
        """
        return self.conf.get("USER", key)

    def get_db(self, key):
        """
        读取配置文件数据库信息
        :param key:
        :return:
        """
        value = self.conf.get("DATABASE", key)
        return value

    def get_email(self, key):
        return self.conf.get("EMAIL", key)

    def get_http(self, key):
        return self.conf.get("HTTP", key)

    # 读取xml语句存储在字典中
    def set_xml(self, xmlPath):
        database = {}
        if len(database) == 0:
            tree = ElementTree.parse(xmlPath)
            for db in tree.findall("database"):
                db_name = db.get("name")
                table = {}
                ss = list(db)
                for tb in ss:
                    table_name = tb.get("name")
                    sql = {}
                    sss = list(tb)
                    for data in sss:
                        sql_id = data.get("id")
                        sql[sql_id] = data.text
                    table[table_name] = sql
                database[db_name] = table
        return database

    # 从xml中获取sql语句
    def get_sql(self, database_name, table_name, sql_id):
        database = self.set_xml(self.sqlXmlPath)
        sql_ele = database.get(database_name).get(table_name).get(sql_id)
        sql = str(sql_ele).replace('  ', '', 60)
        return sql

    # 从excel中读取数据
    def get_xls(self, xlsPath, sheet_name, firstCellInfo):
        cls = []
        file = open_workbook(xlsPath, encoding_override='utf-8')
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'%s' % firstCellInfo:
                cls.append(sheet.row_values(i))
        return cls

    # 从excel中读取测试数据
    def get_caseInfo(self, sheet_name, ):
        cls = self.get_xls(self.testCaseExcelPath, sheet_name, "case_name")
        return cls


if __name__ == "__main__":
    u = util()
    s = u.get_http("timeout")
    s1 = u.get_user("username")
    s2 = u.get_db("port")
    s3 = u.get_email("To")

    ss = u.get_sql("new111", "table000", "select_num")

    sss = u.get_caseInfo("login")

    print(s, s1, s2, s3, ss, sss)
