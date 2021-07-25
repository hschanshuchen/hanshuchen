import pymysql

from src.Common.Log import MyLog
from src.Common.util import util


class DataBase:
    global host , username , password , port , database , config
    host=util().get_db("host")
    username=util().get_db("username")
    password=util().get_db("password")
    port=util().get_db("port")
    database=util().get_db("db_name")
    config={"host":str(host),'user':username,'password':password,'port':int(port),'db':database,'charset':'utf8'}

    def __init__(self):
        self.log=MyLog().get_log()
        self.logger=self.log.logger
        self.db=None

    def connectDB(self):
        try:
            self.db=pymysql.connect(**config)
            self.cursor=self.db.cursor()
        except ConnectionError as ex:
            self.logger.info("111111")
            self.logger.error(str(ex))

    def executeSQL(self,sql,params):
        self.connectDB()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def get_all(self):
        value=self.cursor.fetchall()
        return value

    def get_one(self):
        value = self.cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()


if __name__=="__main__":

    m= DataBase()
    cur=m.executeSQL("SELECT * FROM stu;",' ')
    all=m.get_all()
    print(all)
    print(all[0])
