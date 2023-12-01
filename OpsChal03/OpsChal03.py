#-401 Ops Challenge 3-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-Author: Samuel Allan------------------------------------------------------------------------------------------------------------------------------------------------------------
#-Date of last revision: 10/28/2023-----------------------------------------------------------------------------------------------------------------------------------------------
#-Purpose: In Python, add the below features to your uptime sensor tool.----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------The script must:-------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----Ask the user for an email address and password to use for sending notifications.---------------------------------------------------------------------------------------------
#----Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).-------------------------------------------------------------------------
#----Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.--------------------------------------------------------
#--------Important Notes----------------------------------------------------------------------------------------------------------------------------------------------------------
#------------DO NOT commit your email password in plain text within your script to GitHub as this easily becomes public.----------------------------------------------------------
#------------Create a new “burner” account for this exercise. Do not use an existing email account.-------------------------------------------------------------------------------
#-Stretch Goals (Optional Objectives)---------------------------------------------------------------------------------------------------------------------------------------------
#----In Python, add the below features to your uptime sensor tool.----------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----Append all status changes to an event log. Each event must include a timestamp, event code, any host IP addresses involved, and a human readable description.----------------
#----Check for BURNER_EMAIL_ADDRESS and BURNER_EMAIL_PASSWORD environment variables (eg: loaded from .profile). If found, the script skips requesting credentials via user input.-
#----Alternatively, send the notification email from a cloud mailer service (like Mailgun, or AWS SES), instead of SMTP through your burner address.------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Import space
import smtplib
import ssl
from email.message import EmailMessage
import os
import time
import datetime

# Variables
email_receiver = None #defining email receiver as an empty variable now so we can take input for it only if needed.
persistent_mode = False #indicates whether or not persistent mode has been enabled by the user

#the big function, the big boy, makes it email.
def send_email(email_type, receiver):
    email_sender = os.getenv('BURNER_EMAIL_ADDRESS')
    email_password = os.getenv('BURNER_EMAIL_PASSWORD')
    receiver_email = receiver

    if email_type == "confirmation":
        subject = "You've turned on email notifications for UpSense"
        body = "This email is to confirm that you have turned on email notifications for UpSense, the open source uptime detector. If you have received this email in error, or did not turn on email notifications for Upsense, please reply to this email with a brief summary of your issue, and a customer service agent will be in contact with you shortly!"
    elif email_type == "status_change":
        subject = "Your monitored IP is down! (" + hostname + ")"
        body = "The IP address (" + hostname + ") you've chosen to monitor is down! This may call for immediate attention depending on your need for this service. If you find this report was issued in error, or did not turn on email notifications for Upsense, please reply to this email with a brief summary of your issue, and a customer service agent will be in contact with you shortly!"

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = email_sender
    msg["To"] = receiver_email

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_sender, email_password)
            server.send_message(msg)  
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

#different types of yes and no for error handling in user input.
yes_forms = ["Y", "y", "YES", "yes", "yES", "Yes", "YeS", "yeS", "yEs", "YEs"]
no_forms = ["N", "n", "NO", "no", "No", "nO"]
#user input here will set the running mode.
decision = input("Would you like to enable Email notifications? This will automatically enable persistent mode as well. y/n: ")
if decision in yes_forms:
    print("Email:", os.getenv('BURNER_EMAIL_ADDRESS'))
    print("App Password:", os.getenv('BURNER_EMAIL_PASSWORD'))

    #if the user said yes, enable persistent mode, allowing the program to run continuously and send email updates.
    persistent_mode = True
    email_receiver = input("please provide an email address, a confirmation email will be sent: ")
    send_email("confirmation", email_receiver)

hostname = input("Provide an IP address: ")  # Storing the host in input for now
output_file = input("Provide a name for your text log: ")

if not persistent_mode:
    numbah = input("Provide the length of time to run in minutes: ")
    number = float(numbah)  # Convert to an integer
    # Calculate the end time based on the current time and the specified duration
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=number)



# MAIN:
last_status = None
try:
    with open(output_file, "a") as f:
        while persistent_mode or datetime.datetime.now() < end_time:
            # Ping, -c is count, hostname is the target, dev null sends terminal output to the abyss
            response = os.system(f"ping -c 1 {hostname} > /dev/null 2>&1")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if response == 0:  # If there's a positive response,
                status = "UP"
            else:
                status = "DOWN"

            if last_status is not None and status != last_status:

                if persistent_mode:
                    send_email("status_change", email_receiver)

            last_status = status

            result = f"{timestamp}, {hostname}, {status}\n"
            # print(result)  # Printing result to the terminal (commented out for real-world use)
            f.write(result)  # Writing result to the file
            time.sleep(2)  # Wait 2 seconds before looping
except Exception as e:
    print(f"An error occurred: {e}")
