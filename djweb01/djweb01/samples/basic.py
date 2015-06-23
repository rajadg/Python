'''
Created on 23-Jun-2015

@author: dgraja
'''

from django.http import HttpResponse
from djweb01.samples.Node import *


def basic01(request):
    return HttpResponse("Basic Sample 01 <br/> Hello World !!")

def basic02(request):
    response = Html(title='Basic Sample 02')
    response.body().\
        append(h1().append('basic sample 02')).\
        append(para().append('Hello World !!'))
    return HttpResponse(str(response))

def basic03(request, arg):
    response = Html(title='Basic Sample 03')
    response.body().\
        append(h1().append('basic sample 03')).\
        append(para().append('Query is %s' % arg))
    return HttpResponse(str(response))

if __name__ == '__main__':
    pass