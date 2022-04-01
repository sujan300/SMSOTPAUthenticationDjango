from django.shortcuts import render,HttpResponse

# Create your views here.
from twilio.rest import Client

import random



def send_sms(request):

    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'AC5cde9775cac8c2cbea1b1f2a0bcf08a3'
    auth_token = '5ceeadc4f758ab759d9f105d1c37dbfc'
    
    client = Client(account_sid, auth_token)

    otp=random.randint(50000, 100000)
    print(f"this is the otp number is {otp}")
    
    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_='+17655713878',
                                body =f'please verify your phone number add this number on the app {otp}',
                                to ='+9779845674021'
                            )
    
    print(message.sid)

    return HttpResponse(message.sid)