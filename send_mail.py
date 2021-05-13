from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from email.mime.application import MIMEApplication
import smtplib
from datetime import datetime



class SendMail:

    def __init__(self,receive_email):
        self.email = "public@styd.cn"
        self.pwd = "Yw112135"
        self.receive_email = receive_email

    def send_content(self,receiver_name="数据迁移者",title="数据迁移导出",content_1="",file_path=""):

        now = str(datetime.now())[:19]
        content = "FYI ,\n\t%s附件是你提交的导出任务的数据，请注意查收，如有问题请联系管理员！"%content_1

        msg = MIMEMultipart()
        msg['From'] = self.format_address("<%s>" % self.email)
        msg['To'] = self.format_address("%s<%s>" % (receiver_name,self.receive_email))
        msg['Subject'] = Header(title, 'utf-8').encode()

        zipApart = MIMEApplication(open(file_path, 'rb').read())
        zipFile = file_path.split("/")[-1]
        zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        # 邮件正文是MIMEText:
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        msg.attach(zipApart)
        # 配置服务, 默认端口25
        smtp_server = "smtp.exmail.qq.com"
        server = smtplib.SMTP(smtp_server, 25)
        server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        server.starttls()

        server.login(self.email, self.pwd)
        server.sendmail(self.email, [self.receive_email], msg.as_string())
        server.quit()

    def send_error(self,receiver_name="数据迁移者",title="数据迁移导出",content="",cc_email=None):
        # now = str(datetime.now())[:19]
        # content = "管理员服务挂了！%s" % now

        msg = MIMEMultipart()
        msg['From'] = self.format_address("<%s>" % self.email)
        msg['To'] = self.format_address("%s<%s>" % (receiver_name, self.receive_email))
        to_address = [self.receive_email]
        if cc_email !=None:
            msg['Cc'] = cc_email
            to_address = [self.receive_email] + cc_email.split(',')
            # msg.add_header('Cc', cc_email)
        msg['Subject'] = Header(title, 'utf-8').encode()

        # 邮件正文是MIMEText:
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        # 配置服务, 默认端口25
        smtp_server = "smtp.exmail.qq.com"
        server = smtplib.SMTP(smtp_server, 25)
        server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        server.starttls()

        server.login(self.email, self.pwd)
        server.sendmail(self.email, to_address, msg.as_string())
        server.quit()

    def format_address(self,s):
        name, address = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), address))


# email = SendMail('1223571195@qq.com')
# email = SendMail('hechengcheng@styd.cn')
# email.send_error(receiver_name="Double",title="测试身_20200829155855.zip")

