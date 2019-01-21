#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import user


def send_email():
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(user.email_username, user.email_password)
    sender = user.email_username
    receiver = '617017840@qq.com'
    subject = 'Python email test'
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = '18924919769@163.com <18924919769@163.com>'
    msg['To'] = '617017840@qq.com'
    msg['Date'] = '2019-01-21'

    text = "Congratulation! You have submit the order! (python email test)"
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    send_email()
