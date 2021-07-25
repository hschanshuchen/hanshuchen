import logging
import os
import threading
from datetime import datetime

class Log:
    def __init__(self):
        global logPath, resultPath
        resultPath=os.path.realpath("./../result/log")
        print(resultPath)
        if not os.path.exists(resultPath):
            os.makedirs(resultPath)
        logPath=os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')

        # 输出到文件中
        handler = logging.FileHandler(os.path.join(logPath,"outPut.log"))
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

class MyLog:
    log = None
    mutex = threading.Lock()
    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log



if __name__=='__main__':

    log=MyLog().get_log()
    log.logger.info("111111111")