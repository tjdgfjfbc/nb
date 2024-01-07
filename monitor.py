import schedule
import time
import psutil
import smtplib
from email.mime.text import MIMEText

# 监控项
app_pid = 206093  # 替换成您要监控的进程PID

# 邮件配置
mail_host = "您的SMTP邮件服务器的主机名或IP地址"
mail_port = SMTP邮件服务器的端口号
mail_user = "用于身份验证的发件人邮箱地址" 
mail_pass = "发件人邮箱密码或授权码"
mail_receivers = ["接收邮箱"]

# 检查进程
def check_app():
    return psutil.pid_exists(app_pid)

# 发送邮件报警
def send_mail(subject, content):
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = mail_user

    server = smtplib.SMTP(mail_host, mail_port)
    server.ehlo()
    server.starttls()
    server.login(mail_user, mail_pass)

    for receiver in mail_receivers:
        server.sendmail(mail_user, receiver, msg.as_string())

    server.quit()

# 定时任务  
def job():
    if not check_app():
        send_mail("App节点断了 Down", f"App with PID {app_pid} is down!")
    else:
        print("App is running")

schedule.every(60).seconds.do(job)  # 每60秒运行一次检查你也可以自己设置多少秒检查一次修改60就可以了

while True:
    schedule.run_pending()
    time.sleep(1)
