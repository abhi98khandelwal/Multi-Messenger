from Tkinter import *
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import getpass

print "Welcome to messenger: FB / Gmail / SMS" 
your_adr = raw_input("Your email ID: ")
rec_adr = raw_input("Receiver's email ID: ")

msg = MIMEMultipart()

subj = raw_input("Subject: ")
msg['From'] = your_adr
msg['To'] = rec_adr
msg['Subject'] = subj

body = raw_input(" Text you want to enter ")

msg.attach(MIMEText(body, 'plain'))

strings = raw_input("Enter file address: ")
attachment = open(strings, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename = %s" % strings)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_adr, getpass.getpass())
text = msg.as_string()
server.sendmail(your_adr, rec_adr, text)
server.quit()
