import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From']='Sender Email'
email['To']='Recepient Email'
email['Subject']='Subject'

email.set_content(html.substitute({'name':'#FILL NAME'}),'html')

#this is customizable for each host server(gmail,outlook,etc..)
with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp: 
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Sender Email','Sender Password')
    smtp.send_message(email)
