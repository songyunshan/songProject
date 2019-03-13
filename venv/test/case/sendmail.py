# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#------------跟发邮件相关的参数---------
smtpserver = "smtp.163.com" #发件服务器
port = 25 #端口号
sender = "songyunshan90@163.com"#账号
psw = "song4465" #此处 为 授权码
receiver = "songyunshan90@163.com" #接收人
#-------------编辑邮件的内容------------
subject = "sys测试主题163"
#读取文件
file_path = "C:\\Users\\sys\\PycharmProjects\\songNewProject\\venv\\test\\report\\result.html"
with open(file_path,"rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg['from'] = sender
msg['to']=receiver
msg['subject'] = subject
#正文
body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)
# msg['from']=sender
# msg['to']=receiver
# msg['subject']=subject
#附件
att =MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename = "test_report.html"'
msg.attach(att)

#发送邮件
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver) #连接服务器
    smtp.login(sender,psw) #登录
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string()) #发送
smtp.quit()#关闭


