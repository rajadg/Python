'''
Created on 05-May-2016

@author: dgraja
'''

from django.shortcuts import render
from django.core.mail import send_mail


def compose_email(request):
    """
        Compose and send emails
    """
    data = {"sender": "",
            "to": "",
            "cc": "",
            "subject": "",
            "body": ""}
    if request.POST:
        for key in data.keys():
            if key in request.POST:
                data[key] = request.POST[key]
        if "send" in request.POST and request.POST["send"] == "send":
            # Code to send the email
            print data
#             send_mail(subject=data["subject"],
#                       message=data["body"],
#                       from_email=data["sender"],
#                       recipient_list=data["to"].replace(',', ';').split(';'))
            pass

    return render(request, "simple/send_mail.html", data)
