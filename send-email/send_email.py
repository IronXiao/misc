#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def send_email_by_smtp(email_sender, email_server_host, email_server_user, email_server_pwd, to: str, title, content):
    import smtplib
    from email.message import EmailMessage
    to = to.split(';')
    message = EmailMessage()
    message['Subject'] = title
    message['From'] = email_sender
    message['To'] = to
    message.set_content(content)
    try:
        server = smtplib.SMTP(email_server_host)
        server.ehlo()
        server.starttls()
        server.login(email_server_user, email_server_pwd)
        server.send_message(message)
        server.quit()
        print('email send success!')
    except Exception as e:
        print('email send err:', e)


if __name__ == '__main__':
    if len(sys.argv) == 8:
        _, email_sender, email_server_host, email_server_user, email_server_pwd, to, title, content = sys.argv
        send_email_by_smtp(email_sender, email_server_host,
                           email_server_user, email_server_pwd, to, title, content)
    else:
        print('must need 7 args !!!')
