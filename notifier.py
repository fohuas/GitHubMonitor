import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Notifier:
    def __init__(self):
        # 配置邮件服务器
        self.smtp_server = 'smtp.example.com'
        self.smtp_port = 587
        self.username = 'your_email@example.com'
        self.password = 'your_email_password'

    def send(self, report):
        message = MIMEText(report, 'plain', 'utf-8')
        message['From'] = Header("GitHub Monitor", 'utf-8')
        message['To'] = Header("User", 'utf-8')
        message['Subject'] = Header("GitHub 仓库更新报告", 'utf-8')

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, [self.username], message.as_string())
            server.quit()
            print("邮件发送成功")
        except Exception as e:
            print(f"邮件发送失败: {e}")