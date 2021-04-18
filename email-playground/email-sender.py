import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Yura Mishin'
email['to'] = 'user@mail.ru'
email['subject'] = 'Hello Email!'

email.set_content('Hello dude!')

with smtplib.SMTP(host='smtp.mailtrap.io', port=2525) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('login', 'password')
    smtp.send_message(email)
    print('Email is sent')
