import requests

from src.Common import Log
from src.Common.configDB import ReadConfig

localReadConfig=ReadConfig()
class configHttp:
    def __init__(self):
        global host,port,timeout
        host=localReadConfig.get_http("basePath")
        port=localReadConfig.get_http("port")
        timeout=localReadConfig.get_http("timeout")
        self.log=Log.get_log()
        self.logger=self.log.logger
        self.header={}
        self.params={}
        self.data={}
        self.url=None
        self.files={}

    def set_url(self,url):
        self.url=host+url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # get请求方法
    def get(self):
        try:
            response=requests.get(self.url,params=self.params,headers=self.headers,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None
    # post请求方法
    def post(self):
        try:
            response=requests.get(self.url,params=self.params,headers=self.headers,files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None
