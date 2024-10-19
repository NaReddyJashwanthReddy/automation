import os
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(reciver,subject,body,attachment=None):
    sender='tangwulinggd@gmail.com'
    password='mwkp lpak bosv zyat'

    #message body and server
    message=MIMEMultipart()
    message['From']=sender
    message['To']=reciver
    message['Subject']=subject

    #attach body
    message.attach(MIMEText(body))

    if attachment:
        attachment_name=os.path.basename(attachment)
        attch=MIMEBase('application','octet-stream')
        with open(attachment,'rb') as file:
            attch.set_payload(file.read())
        encoders.encode_base64(attch)
        attch.add_header('content-Disposition',f'attachment;filename={attachment_name}')
        message.attach(attch)
    
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login(sender,password)
        text=message.as_string()
        server.sendmail(sender,reciver,text)
        print('email sent to reciver')


reciver='20211a0264@bvrit.ac.in'
subject='Day 2 automation with attachment'
body='am sending an attachment'
attachment=r'..\DeclarationFinance (1) (1).pdf'

send_mail(reciver=reciver,subject=subject,body=body,attachment=attachment)