import pymysql

from common.Log import MyLog
from readconfig import ReadConfig
ReadConfig=ReadConfig()

class MyDB:
    global host , username , password , port , database , config
    host=ReadConfig.get_db("host")
    username=ReadConfig.get_db("username")
    password=ReadConfig.get_db("password")
    port=ReadConfig.get_db("port")
    database=ReadConfig.get_db("database")
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

    m=MyDB()
    cur=m.executeSQL("SELECT * FROM stu;",' ')
    all=m.get_all()
    print(all)
    print(all[0])
