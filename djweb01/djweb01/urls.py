from django.conf.urls import patterns, include, url
from django.contrib import admin
from djweb01.samples import basic
from djweb01.samples import table


urlpatterns = [
    url(r'^samples/basic01', basic.basic01),
    url(r'^samples/basic02/$', basic.basic02),
    url(r'^samples/basic03/(?P<arg>(\d|\w)+)/$', basic.basic03),
    url(r'^samples/basic04', basic.basic04),
    url(r'^samples/basic05', basic.basic05),
    url(r'simple/table01', table.simple_table),
    url(r'^admin/', include(admin.site.urls)),
]
