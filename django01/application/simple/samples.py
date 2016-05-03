"templates/simple/welcome.html"'''
Created on 03-May-2016

@author: dgraja
'''
import os
import json
from django.shortcuts import render
from django01.settings import BASE_DIR


def welcome_page(request):
    print "Loading template from %s/%s ..." % (BASE_DIR, "simple/table01.html")
    meta = dict([(key, val) for key, val in request.META.iteritems() if isinstance(val, str) and key not in os.environ.keys()])
    misc = {"cookies": request.COOKIES,
            "user": str(request.user),
            "path": str(request.path),
            "method": request.method,
            "body": str(request.body),
            "query": dict(request.GET),
            "client-address": request.META["REMOTE_ADDR"]}
    data = {"raw_json": json.dumps(meta, indent=4),
            "misc": json.dumps(misc, indent=4)}
    return render(request, "simple/welcome.html", data)


if __name__ == '__main__':
    pass