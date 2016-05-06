'''
Created on 04-May-2016

@author: dgraja
'''

from django.shortcuts import render, redirect
from django01.settings import BASE_DIR
from application import models


def contact_view(request):
    """
        displays contact view
    """
    data = {"name": "",
            "email": "",
            "phone": "",
            "target": "",
            "action": "",
            "activity": "",
            "action_icon": "glyphicon-floppy-disk"}
    if request.POST:
        for key in data.keys():
            if key in request.POST:
                data[key] = request.POST[key]
    if data["activity"] == "":
        data["activity"] = "add"

    if data["action"] == "add" and data["activity"] == "add":
        posted = models.Contact()
        posted.name = data["name"]
        posted.email = data["email"]
        posted.phone = data["phone"]
        posted.save()
    if data["action"] == "add" and data["activity"] == "save":
        posted = models.Contact.objects.get(id=int(data["target"]))
        posted.name = data["name"]
        posted.email = data["email"]
        posted.phone = data["phone"]
        posted.save()
    elif data["action"] == "edit" and data["target"]:
        data["activity"] = "save"
        to_edit = models.Contact.objects.get(id=int(data["target"]))
        data["name"] = to_edit.name
        data["phone"] = to_edit.phone
        data["email"] = to_edit.email
    elif data["action"] == "remove" and data["target"]:
        to_edit = models.Contact.objects.filter(id=int(data["target"]))
        to_edit.delete()
    elif request.POST:
        redirect("/index")

    if data["action"] != "edit":
        data["name"] = data["phone"] = data["email"] = ""
        data["target"] = 0
        data["activity"] = "Add"
        data["action_icon"] = "glyphicon-plus"


    def make_contact(row):
        make_contact.counter = make_contact.counter + 1
        return {'name': row.name, "id": row.id, "email": row.email, "phone": row.phone, "sno": make_contact.counter}
    make_contact.counter = 0

    rows = list([make_contact(row) for row in models.Contact.objects.all()])
    data["items"] = rows

    return render(request, "simple/contacts.html", data)
