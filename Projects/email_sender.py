from email.message import EmailMessage
from password import password
import ssl, smtplib

email_sender = 'Martinscode33@gmail.com'
email_password = password()

# email_receiver = 'niwamag762@civikli.com'
# subject = "Don't forget to subscribe"
# body = """
# Journey to be a Master Python Programmer
# """
email_receiver = input('Enter Email :')
subject = input("Enter Subject: ")
body = input("""Body: 

""")

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())
