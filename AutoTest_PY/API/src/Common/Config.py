import configparser
import os


class Config:
    def __init__(self):
        self.configPath = os.path.abspath(os.path.dirname(__file__)).split('src')[0]+'src\config.ini'
        print(self.configPath)
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