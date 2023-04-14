# 发送邮件

## 准备工作

找一个邮件平台开启`POP3/SMTP服务`获取相关信息

如以下是网易163 邮箱的一个示例

```shell
EMAIL_SENDER = 'xxxyyy@163.com'  # 邮件发送者
EMAIL_RECEIVER = "a@amail.com;b@bmail.com"   # 用";" 英文分号分隔
EMAIL_SERVER_HOST = 'smtp.163.com'  # 邮件服务 host
EMAIL_SERVER_USER = 'xxxyyy'  # 邮件服务登录用户名
EMAIL_SERVER_PASSWORD = 'FKSUKHZLPAINYEXC'  # 邮箱登录授权码
```

## 发送邮件

```shell
python3 send_email.py email_sender email_server_host email_server_user email_server_pwd to title content
```

如：

```shell
python3 send_email.py "????@163.com" "smtp.163.com" "bugtracker_test" "???????????" "???@gmail.com;???@msn.cn" "Test" "This is a test mail"
email send success!
```

注意：上述`???`皆为混淆后的信息，请以自己的为准。

