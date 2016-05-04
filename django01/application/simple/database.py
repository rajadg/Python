'''
Created on 04-May-2016

@author: dgraja
'''

from django.shortcuts import render
from django01.settings import BASE_DIR
from application import models


def contact_view(request):
    """
        displays contact view
    """
    name = email = phone = ""
    if request.POST:
        if "name" in request.POST:
            name = request.POST["name"]
        if "email" in request.POST:
            email = request.POST["email"]
        if "phone" in request.POST:
            phone = request.POST["phone"]
        if "add" in request.POST and request.POST["add"] == "Add":
            ct = models.Contact()
            ct.name = name
            ct.email = email
            ct.phone = phone
            ct.save()

    def make_contact(row):
        return {'name': row.name, "id": row.id, "email": row.email, "phone": row.phone}

    rows = list([make_contact(row) for row in models.Contact.objects.all()])
    data = {"name": name,
            "email": email,
            "phone": phone,
            "items": rows}


    return render(request, "simple/contacts.html", data)
