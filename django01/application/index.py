'''
Created on 03-May-2016

@author: dgraja
'''
import os
import re
import json
from django.shortcuts import render
from django01.settings import BASE_DIR
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver


all_urls = {"patterns": None}


class Entry(object):
    def __init__(self, title, url, impl):
        self.title = title
        self.url = url
        self.impl = impl


def format_text(text):
    text = re.sub('\n\s+', '\n', text)
    return text


def index_page(request):
    """
        Retrieves the index page (all urls configured in the application)
    """
    print "Loading template from %s/%s ..." % (BASE_DIR, "index.html")
    items = []
    for url in all_urls["patterns"]:
        if isinstance(url, RegexURLPattern):
            items.append(Entry(url.callback.func_name, url.regex.pattern.lstrip('^').rstrip('$'), format_text(url.callback.func_doc)))
        elif isinstance(url, RegexURLResolver):
            patterns = [url.regex.pattern + item.regex.pattern for item in url.url_patterns]
            items.append(Entry(url.app_name,
                               url.regex.pattern.lstrip('^'),
                                "supported urls:" + format_text(json.dumps(patterns, indent=4))))
    data = {"urls": items}
    return render(request, "index.html", data)


if __name__ == '__main__':
    pass