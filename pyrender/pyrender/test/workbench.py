'''
Created on 02-Aug-2015

@author: dgraja
'''

from django.http import HttpResponse
from django.http.request import QueryDict
from django.template import RequestContext, loader

from pyrender.html.Node import *

__counter__ = 0

def get_count():
    global __counter__
    __counter__ = __counter__ + 1
    return __counter__

def counter(request):
    result = Html(title='Sample for Counter !!')
    result.body().append(h3().set_inner_text('Sample for Counter !!'))
    result.body().append(pre(children=['counter: %3d' % get_count()]))
    response = str(result)
    return HttpResponse(response)

def recorder(request):
    if not request.session.get('data'):
        request.session['data'] = list()
    data = request.session['data'] 
    data.append(str(get_count()))
    request.session['data'] = data
    result = Html(title='Sample for Recorder !!')
    result.body().append(h3().set_inner_text('Sample for Recorder !!'))
    info = "Data : %r" % data
    result.body().append(para().set_inner_text(info))
    response = str(result)
    return HttpResponse(response)
    