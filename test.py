import smtplib
import ssl
from email.message import EmailMessage

yes_forms = ["Y", "y", "YES", "yes", "yES", "Yes", "YeS", "yeS", "yEs", "YEs"]
no_forms = ["N", "n", "NO", "no", "No", "nO"]
decision = input("Would you like to enable Email notifications? This will automatically enable persistent mode as well. y/n: ")
if decision in yes_forms:
    email_sender = 'burnr.numbah2@gmail.com'
    email_password = 'itdo vuuu czta qisp'
    email_receiver = input("please provide an email address, a confirmation email will be sent: ")
    subject = "You've turned on email notifications for UpSense"
    body = "This email is to confirm that you have turned on email notifications for UpSense, the open source uptime detector. If you have received this email in error, or did not turn on email notifications for Upsense, please reply to this email with a brief summary of your issue, and a customer service agent will be in contact with you shortly!"
hostname = input("Provide an IP address: ")  # Storing the host in input for now
output_file = input("Provide a name for your text log: ")
numbah = input("Provide the length of time to run in minutes: ")
number = float(numbah)  # Convert to an integer

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.send_message(em)