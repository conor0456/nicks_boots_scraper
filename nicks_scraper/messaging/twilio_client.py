import os
from twilio.rest import Client
from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

account_sid = config('TWILIO_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
email_token = config('TWILIO_EMAIL_TOKEN')
from_phone_number = config('TWILIO_PHONE_NUMBER')
to_phone_number = config('NOTIFICATION_PHONE_NUMBER')
client = Client(account_sid, auth_token)

def send_message(new_products):
     content = "\n".join(new_products)
     client.messages \
                .create(
                     body=content,
                     from_=from_phone_number,
                     to=to_phone_number
                 )
     print("Sent message: \n" + content)

def send_email(new_products):
     content = "\n".join(new_products)
     message = Mail(
          from_email='conor0456@gmail.com',
          to_emails='conor0456@gmail.com',
          subject='New Nicks boots in stock!',
          html_content="\n".join(new_products))
     sg = SendGridAPIClient(email_token)
     response = sg.send(message)
     print("Sent message: \n" + content)

def notify(new_products):
     send_email(new_products)
     send_message(new_products)