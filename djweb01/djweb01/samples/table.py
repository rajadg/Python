'''
Created on 03-May-2016

@author: dgraja
'''
import os
from django.shortcuts import render
from djweb01.settings import BASE_DIR


def simple_table(request):
    print "loading template from %s/%s" % (BASE_DIR, "templates/simple/table01.html")
    return render(request, "templates/simple/table01.html", {})


if __name__ == '__main__':
    pass