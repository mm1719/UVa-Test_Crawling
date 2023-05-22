import smtplib
import sys
from smtplib import SMTP

From = 'sending.account@gmail.com' # Please Change
Password = 'yourpassword'          # Please Change
To = 'receiving.account@gmail.com' # Please Change

line = sys.stdin.read()

smtp_server = 'smtp.gmail.com'
smtp_port = 587

smtpObj = smtplib.SMTP(smtp_server, smtp_port)
smtpObj.starttls()
smtpObj.login(From,Password)
to = [To]
msg = line

smtpObj.sendmail(From, to, msg)
smtpObj.quit()
