import os
from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
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

def send():
     client.messages \
                .create(
                     body="https://nicksboots.com/rts-4844/",
                     from_=from_phone_number,
                     to=to_phone_number)