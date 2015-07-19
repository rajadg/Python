'''
Created on 23-Jun-2015

@author: dgraja
'''

from django.http import HttpResponse
from djweb01.samples.Node import *
from django.http.request import QueryDict
import json


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

def basic04(request):
    qdict = QueryDict(request.META['QUERY_STRING'])
    response = Html(title='Basic Sample 04')
    response.body().\
        append(h1().append('basic sample 04')).\
        append(para().append('Query String has %s' % json.dumps(qdict)))
    return HttpResponse(str(response))

def basic05(request):
    req_body = request.read()
    response = Html(title='Basic Sample 05')
    response.body().\
        append(h1().append('basic sample 05')).\
        append(para().append('Request Body is').\
        append(div().append(req_body)))
    return HttpResponse(str(response))

if __name__ == '__main__':
    pass