from django.conf.urls import patterns, include, url
from django.contrib import admin
import djweb01

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djweb01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^samples/basic01', 'djweb01.samples.basic.basic01'),
    url(r'^samples/basic02/$', 'djweb01.samples.basic.basic02'),
    url(r'^samples/basic03/(?P<arg>(\d|\w)+)/$', 'djweb01.samples.basic.basic03'),
    url(r'^samples/basic04', 'djweb01.samples.basic.basic04'),
    url(r'^samples/basic05', 'djweb01.samples.basic.basic05'),
    url(r'^admin/', include(admin.site.urls)),
)
