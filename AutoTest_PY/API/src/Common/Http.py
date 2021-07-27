import requests
import urllib3
from src.Common.Log import Logger
from src.Common.util import util

class Http():
    urllib3.disable_warnings()
    util = util()

    def __init__(self):
        global basicPath, hostIp, timeout
        basicPath = self.util.get_http("basicPath")
        hostIp = self.util.get_http("hostIp")
        timeout = self.util.get_http("timeout")
        self.logger = Logger().get_log().logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.json = {}

    def set_url(self, url):
        self.url = basicPath + hostIp + url
        self.logger.info("url : "+self.url)

    def set_headers(self, headers):
        self.headers = headers
        self.logger.info("headers : "+str(self.headers))

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data
        self.logger.info("data : "+str(self.data))

    def set_json(self, json):
        self.json = json

    def set_files(self, file):
        self.files = file

    # get请求方法
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None

    # post请求方法
    def post(self):
        self.logger.info("method : "+"post")
        try:
            response = requests.post(self.url, data=self.data, json=self.json, headers=self.headers, files=self.files,verify=False)
            # self.logger.info("response : " + response.text)
            return response
        except TimeoutError:
            self.logger.error("Time out")

            return None

    # delete请求方法
    def delete(self):
        try:
            response = requests.delete(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None

    # put请求方法
    def put(self):
        try:
            response = requests.put(self.url, data=self.data, headers=self.headers, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None
