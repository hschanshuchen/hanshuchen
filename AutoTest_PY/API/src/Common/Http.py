import requests
import urllib3

from src.Common.Config import Config
from src.Common.Log import Logger



class Http():
    urllib3.disable_warnings()

    def __init__(self):
        global basicPath, hostIp, timeout
        timeout = Config().get_http("timeout")
        self.logger = Logger().get_log().logger

    # get请求方法
    def get(self, url, headers, cookies, *args):
        try:
            self.logger.info("url: " + url)
            self.logger.info("headers: " + str(headers))
            self.logger.info("cookies: " + str(cookies))
            self.logger.info("params: " + str(args))
            response = requests.get(url, headers=headers, cookies=cookies, timeout=float(timeout), *args)
            self.logger.info("code: " + str(response.status_code))
            self.logger.info("response: " + response.text)

            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None

    # post请求方法
    def post(self, url, headers, cookies, *args):
        self.logger.info("requestMethod : " + "post")
        try:
            self.logger.info("url: " + url)
            self.logger.info("headers: " + str(headers))
            self.logger.info("cookies: " + str(cookies))
            self.logger.info("params: " + str(args))
            response = requests.post(url, headers=headers, cookies=cookies, verify=False, *args)
            self.logger.info("code: " + str(response.status_code))
            self.logger.info("response: " + response.text)
            return response
        except TimeoutError:
            self.logger.error("Time out")

            return None

    # delete请求方法
    def delete(self, url, headers, cookies, *args):
        try:
            self.logger.info("url: " + url)
            self.logger.info("headers: " + str(headers))
            self.logger.info("cookies: " + str(cookies))
            self.logger.info("params: " + str(args))
            response = requests.delete(url, headers=headers, cookies=cookies, timeout=float(timeout))
            self.logger.info("code: " + str(response.status_code))
            self.logger.info("response: " + response.text)
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None

    # put请求方法
    def put(self, url, headers, cookies, *args):
        try:
            self.logger.info("url: " + url)
            self.logger.info("headers: " + str(headers))
            self.logger.info("cookies: " + str(cookies))
            self.logger.info("params: " + str(args))
            response = requests.put(url, headers=headers, cookies=cookies, timeout=float(timeout), *args)
            self.logger.info("code: " + str(response.status_code))
            self.logger.info("response: " + response.text)
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None
