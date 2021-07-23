import configparser
import os


class BasicAction:

    cf = configparser.ConfigParser()

    def __init__(self):
        pass


    def get_config(self , abspath , section , key):
        """
        获取配置文件中的值
        :param abspath:
        :param section:
        :param key:
        :return:
        """
        filePath = os.path.abspath(abspath)
        self.cf.read(filePath, encoding="UTF-8")
        return self.cf.get(section , key)








if __name__== "__main__":
    basicAction = BasicAction()
    value = basicAction.get_config("..\database\config.ini","tester","name")
    print(value)
