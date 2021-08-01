# coding:utf-8
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.Common.Config import Config
from src.Common.Log import Log, Logger


class Email:

    def __init__(self):
        self.logger = Logger().get_log().logger
        self.config = Config()
        self.smtpserver = self.config.get_email("HOST_SERVER")  # 发送邮件的服务器
        self.port = self.config.get_email("port")  # 端口
        self.authorizatioCcode = self.config.get_email("authorizatioCcode")  # QQ授权码，这里填写上自己的授权码

    # 写信流程
    def send_qq_email(self, sender, receiver, subject, fileName):
        msg = MIMEMultipart()
        msg['from'] = sender
        msg['to'] = receiver
        msg['subject'] = subject  # 邮件的主题

        # 通过os获取文件路径
        annex_path = os.path.realpath("../result/report/%s" % fileName)  # 附件内容的路径
        annex = open(annex_path, "r", encoding="utf-8").read()
        main_path = os.path.realpath("../Run/TextTestReport.text")  # 正文内容的路径
        main_body = open(main_path, "r", encoding="utf-8").read()

        # 添加正文到容器
        body = MIMEText(main_body, "plain", "utf-8")
        msg.attach(body)

        # 添加附件到容器
        att = MIMEText(annex, "base64", "utf-8")
        att["Content-Type"] = "application/octet-sream"
        att["Content-Disposition"] = 'attachment;filename=%s' % fileName
        msg.attach(att)

        # 连接发送邮件
        smtp = smtplib.SMTP_SSL(self.smtpserver, self.port)
        smtp.login(sender, self.authorizatioCcode)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()


if __name__ == "__main__":
      qq = Email()
      qq.send_qq_email("2427697226@qq.com", "2427697226@qq.com", "这是一个测试报告", "*.html")

    # root_path = os.path.abspath(os.path.dirname(__file__)).split('src')[0]+'src\config'
    # print(root_path)
