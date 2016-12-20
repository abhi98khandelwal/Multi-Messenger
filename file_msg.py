from Tkinter import *
from twilio.rest import TwilioRestClient
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import getpass
import fbchat

print """-------------------------------------------------------------------------
		------------------------------------------
		|	WELCOME TO MULTIMESSENGER    		  
		|								 
		|	BUILT BY:					 
		|		Krutika Bapat			 
		|		Kushashwa Ravi Shrimali
		|								 		
		|	Undergraduate Students at:	 		  
		|		IIIT NAYA RAIPUR		 		 
		|		(B.Tech CSE)			 		 
		------------------------------------------
-------------------------------------------------------------------------"""
# DETAILS - Email
print "-------------------------------------------------------------------------"
print 'Enter your Email-ID details' 
print "-------------------------------------------------------------------------"

your_adr = raw_input("Your email-ID: ")
pass_adr = getpass.getpass()

# DETAILS - Facebook Message

print "-------------------------------------------------------------------------"
print 'Enter your Facebook Details'
print "-------------------------------------------------------------------------"
your_id = str(raw_input("Enter your username: "))
pass_fb = getpass.getpass()

# DETAILS - SMS 

print "-------------------------------------------------------------------------"
print 'Enter your SMS Details'
print "-------------------------------------------------------------------------"

ACCOUNT_SID = raw_input("Account SID: ") # <auth sid>
AUTH_TOKEN = raw_input("Account Token: ") # <auth token>
fromNumber = str(raw_input("Enter your number: "))
exit_input = raw_input("""If you want to exit, type "EXIT", if not, type anything else.""")
while(exit_input != "EXIT"):
	# MENU
	print " EMAIL [1]  |  FACEBOOK MESSAGE [2] |  SMS [3] " 

	number = int(raw_input("Menu Selection: "))

	if(number == 1):
	  rec_adr = raw_input("Receiver's email ID: ")

	  msg = MIMEMultipart()

	  subj = raw_input("Subject: ")
	  msg['From'] = your_adr
	  msg['To'] = rec_adr
	  msg['Subject'] = subj

	  body = raw_input("Text you want to enter: ")

	  msg.attach(MIMEText(body, 'plain'))

	  strings = raw_input("Enter file address: ")
	  if(strings != ''):
		  attachment = open(strings, "rb")
		  part = MIMEBase('application', 'octet-stream')
		  part.set_payload((attachment).read())
		  encoders.encode_base64(part)
		  part.add_header('Content-Disposition', "attachment; filename = %s" % strings)
			
		  msg.attach(part)

	  server = smtplib.SMTP('smtp.gmail.com', 587)
	  server.starttls()
	  server.login(your_adr, pass_adr)
	  text = msg.as_string()
	  server.sendmail(your_adr, rec_adr, text)
	  server.quit()
	  
	# FB CHAT
	elif(number == 2):
	  client = fbchat.Client(your_id, pass_fb);
	  print "Type your friend's name: "
	  fname = str(raw_input("Enter friend's name: "))
	  friends = client.getUsers(fname)

	  friend = friends[0]
	  messagetosend = str(raw_input("Message to send: "))
	  sent = client.send(friend.uid, messagetosend)
	  if sent:
		print("Message sent successfully")
	  else:
		print("Not sent")
		
	# SMS 
	elif(number == 3):
	  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	  # Input details
	  ToNumber = str(raw_input("Enter the number you want to send SMS: "))
	  bodyText = str(raw_input("Enter text you want to enter: "))
	  client.messages.create(
		to = '+91' + ToNumber,
		from_ = '+' + fromNumber , #<fromNumber>
		body = bodyText,
	  )
	exit_input = raw_input("""If you want to exit, type "EXIT", if not, type anything else.""")

