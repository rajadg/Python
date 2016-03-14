'''
Created on 23-Jun-2015

@author: dgraja
'''

from django.http import HttpResponse
from djweb01.samples.Node import *
from django.http.request import QueryDict
import json


def basic01(request):
    '''
        Simply render the response
    '''
    return HttpResponse("Basic Sample 01 <br/> Hello World !!")


def basic02(request):
    '''
        Simply render a response with some formatting
    '''
    response = Html(title='Basic Sample 02')
    response.body().\
        append(h1().append('basic sample 02')).\
        append(para().append('Hello World !!'))
    return HttpResponse(str(response))


def basic03(request, arg):
    '''
        Render the response with full query string
    '''
    response = Html(title='Basic Sample 03')
    response.body().\
        append(h1().append('basic sample 03')).\
        append(para().append('Query is %s' % arg))
    return HttpResponse(str(response))


def basic04(request):
    '''
        Render the response with values from query string
        logic:
            1. The request.META['QUERY_STRING'] contains the query string
            2. This is a dictionary containing the query as name-value pairs
    '''
    qdict = QueryDict(request.META['QUERY_STRING'])
    response = Html(title='Basic Sample 04')
    response.body().\
        append(h1().append('basic sample 04')).\
        append(para().append('Query String has %s' % json.dumps(qdict)))
    return HttpResponse(str(response))


def basic05(request):
    '''
        Render the response as original request breakup (request headers, request body)
        logic:
            1. The 'request.META'. contains metadata about request, this is a dictionary
            2. All keys starting with HTTP_ in request.META are http request headers.
            3. To get the request body, we need to call 'request.read()' method
    '''
    output = "Request Headers:"
    for key, val in request.META.iteritems():
        if key.startswith("HTTP_"):
            output += "\n<br/>%s: %s" % (key[5:].replace("_", "-").title(), val)
    output += "\n<br/>"
    output += "\n<br/>\n<br/> Body: \n</br> " + request.read().replace("\n", "\n<br/>")
    response = Html(title='Basic Sample 05')
    response.body().\
        append(h1().append('basic sample 05')).\
        append(para().append('Request Body is').
               append(div().append(output)))
    return HttpResponse(str(response))


if __name__ == '__main__':
    pass
