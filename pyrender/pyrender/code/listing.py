'''
Created on 01-Aug-2015

@author: dgraja
'''

from django.http import HttpResponse
from django.http.request import QueryDict
from django.template import RequestContext, loader

from pyrender.html.py2html import py2html
import json
import os
from tokenize import generate_tokens


def showfile(request):
#     qdict = QueryDict(request.META['QUERY_STRING'])
#     response = Html(title='Python source')
#     heading = h1().append('Source Code')
#     response.body().append(h1)
#     lines = read_file()
#     lineno = 0
#     for line in lines:
#         lineno = lineno + 1 
#         response.body().append("<pre>%04d|%s</pre>" % (lineno, line))
        
    return HttpResponse(str(''))

def listfile(request):
    examples = os.path.join(os.path.dirname(__file__), 'examples')
    obj = py2html(os.path.join(examples, 'sample01.py'))
    obj.current_line = 6
    response = obj.render_html_table()
    response = obj.get_style_tag() + response
        
    return HttpResponse(response)


