import glob
import os
import smtplib
import threading
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Log import Log
from src.Common.util import util


class Email:
    util = util()

    def __init__(self):
        global host, username, password, port, sender, title, content
        host = util.get_email("mail_host")
        username = util.get_email("mail_username")
        password = util.get_email("mail_password")
        port = util.get_email("mail_port")
        sender = util.get_email("sender")
        title = util.get_email("subject")
        content = util.get_email("content")
        self.value = util.get_email("receiver")
        self.receiver = []
        for n in str(self.value).split("/"):
            self.receiver.append(n)
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.subject = title + " " + date
        self.log = Log.get_log()
        self.logger = self.log.logger
        self.msg = MIMEMultipart("mixed")

    def config_header(self):
        self.msg["subject"] = self.subject
        self.msg["from"] = sender
        self.msg["to"] = ";".join(self.receiver)

    def config_content(self):
        content_plain = MIMEText(content, "plain", "utf-8")
        self.msg.attach(content_plain)

    def config_file(self):
        if self.check_file():
            reportpath = self.log.get_result_path()
            zippath = os.path.join(os.path.realpath("./../result"), "result", "test.zip")
            files = glob.glob(reportpath + "\*")
            f = zippath.ZipFile(zippath, 'w', zippath.Zip_DEFLATED)
            for file in files:
                f.write(file)
            f.close()
            reportfile = open(zippath, 'rb').read()
            filehtml = MIMEText(reportpath, "base64", 'utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
            self.msg.attach(filehtml)
            print(self.msg)

    def check_file(self):
        reportpath = self.log.get_report_path()
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(username, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            self.logger.error(str(ex))


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    e = Email()
    e.config_file()
