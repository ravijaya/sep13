from smtplib import SMTP
from email.mime.text import MIMEText
# http://collabedit.com/ssfen
SMTPADDRESS = 'localhost'


def send_alert_email(from_address, to_address, subject, message):
    mesg = MIMEText(message)
    mesg['From'] = from_address
    mesg['To'] = to_address
    mesg['Subject'] = subject

    smtp = SMTP(SMTPADDRESS)  # smtp client
    # smtp.login(user, pwd)
    smtp.sendmail(from_address, to_address, mesg.as_string())
    smtp.close()


if __name__ == '__main__':
    send_alert_email('ravi@localhost', 'training@localhost', 'dummy email', 'a sample string')
