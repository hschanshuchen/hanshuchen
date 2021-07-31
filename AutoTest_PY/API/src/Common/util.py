import os
import random
import string
from xml.etree import ElementTree as ElementTree

from xlrd import open_workbook


class util:

    def __init__(self):
        self.testCaseExcelPath = os.path.abspath("../TestData/file/login.xls")
        self.sqlXmlPath = os.path.abspath("../TestData/file/sql.xml")

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

    def getRandomStr(self, n):
        return ''.join(random.sample(string.ascii_letters + string.digits, n))


if __name__ == "__main__":
    u = util()


    ss = u.get_sql("new111", "table000", "select_num")

    sss = u.get_caseInfo("login")

    print( ss, sss)
