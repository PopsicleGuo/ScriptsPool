import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.gmail.com'
mail_user = 'popsicleguo@gmail.com'
mail_pass = 'Mouyiying#840107'
sender = 'alvin.guo@cdprojektred.com'
receivers = ['30040958@qq.com']

message = MIMEText('content', 'plain', 'utf-8')
message['Subject'] = 'title'
message['From'] = sender
message['To'] = receivers[0]

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 587)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(
        sender, receivers, message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error', e)